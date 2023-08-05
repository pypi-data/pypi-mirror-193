import logging
from dataclasses import dataclass, field
from typing import Generic, Callable, Type, Optional, Dict

from aiohttp import client

from .abstraction import AbstractRequestBuilder, TController, AbstractEndpointCollection, AbstractEndpointDef
from .endpoints import EndpointDefTable, BoundEndpoints

log = logging.getLogger(__name__)


class BaseClient:
    def __init__(self, session: client.ClientSession):
        self.session = session


@dataclass
class RequestBuilder(AbstractRequestBuilder):
    url_params: Dict = field(default_factory=dict)
    query: Dict = field(default_factory=dict)
    body: Dict = field(default_factory=dict)
    headers: Dict = field(default_factory=dict)


class ClientClassFactory(Generic[TController]):
    def __init__(self,
                 api_cls: Type[TController],
                 endpoints: AbstractEndpointCollection[TController],
                 client_classname: Optional[str] = None):
        self._api_cls = api_cls
        self._endpoints = endpoints
        self._client_classname = client_classname or (api_cls.__name__.lstrip('Abstract') + 'Client')

    def create_client_class(self) -> Type[TController]:
        return type[TController](
            self._client_classname,
            (BaseClient, self._api_cls,),
            {e.controller_method.__name__: self.create_endpoint_caller(e)
             for e in self._endpoints})

    @staticmethod
    def create_endpoint_caller(endpoint: AbstractEndpointDef):
        """
        Map the endpoint into a method that sends a request to the server and processes
        the response.
        :param endpoint:
        :return:
        """

        async def send(cls: BaseClient, *args, **kwargs):
            req = RequestBuilder()
            endpoint.signature.serialize_args(req, args, kwargs)
            route_path = endpoint.route_path

            for name, val in req.url_params.items():
                route_path = route_path.replace(f'{{name}}', val)

            async with cls.session.request(
                    endpoint.http_method,
                    route_path,
                    params=req.query,
                    json=req.body,
                    headers=req.headers
            ) as resp:
                resp.raise_for_status()
                return await endpoint.signature.deserialize_result(resp)

        return send


ClientFactory = Callable[[client.ClientSession], TController]


def client_factory(api_cls: Type[TController],
                   endpoints: AbstractEndpointCollection[TController] | EndpointDefTable) -> ClientFactory[TController]:
    """
    Generate a client side implementation of the api_cls.

    :param api_cls: the abstract base class of the api shared by client and server.
    :param endpoints: the endpoint definitions.
    """
    if isinstance(endpoints, EndpointDefTable):
        endpoints = BoundEndpoints(api_cls, endpoints)
    client_cls_factory = ClientClassFactory(api_cls, endpoints)
    return client_cls_factory.create_client_class()
