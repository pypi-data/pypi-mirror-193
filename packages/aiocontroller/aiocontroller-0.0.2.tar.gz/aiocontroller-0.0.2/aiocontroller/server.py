import http
import inspect
import logging
from typing import Generic, Callable, Type, Generator, Any, Iterable, Iterator

from aiohttp import web
from di_ioc import AbstractServiceProvider

from .abstraction import TController, AbstractEndpointCollection, AbstractEndpointDef
from .endpoints import EndpointDefTable, BoundEndpoints

log = logging.getLogger(__name__)


def request_scope(req: web.Request) -> AbstractServiceProvider:
    if 'scope' not in req:
        root: AbstractServiceProvider = req.app['service_container']
        scope = root.create_scope()
        req['scope'] = scope
    else:
        scope = req['scope']

    return scope


class ControllerRoutes(Generic[TController], Iterable[web.AbstractRouteDef]):
    """
    Defines how endpoints map to web.AbstractRouteDefs. Many of the steps during
    the process to convert are exposed as methods that can be overridden.
    """

    def __init__(self, endpoints: AbstractEndpointCollection[TController]):
        self._endpoints = endpoints

    def __iter__(self) -> Iterator[web.AbstractRouteDef]:
        return self.create_routes().__iter__()

    def create_route(self, endpoint: AbstractEndpointDef) -> web.AbstractRouteDef:
        return web.route(
            endpoint.http_method,
            endpoint.route_path,
            self.create_req_handler(endpoint))

    def create_routes(self) -> Generator[web.AbstractRouteDef, None, None]:
        for f in self._endpoints:
            yield self.create_route(f)

    def create_req_handler(self, endpoint: AbstractEndpointDef):
        async def req_handler(req: web.Request) -> web.Response:
            with request_scope(req):
                controller = self.create_controller(req)
                try:
                    result = await self.call_handler_method(endpoint, controller, req)
                    return self.create_response(endpoint, result)
                except BaseException as e:
                    return self.create_error_response(endpoint, e)

        return req_handler

    def create_controller(self, req: web.Request) -> TController:
        return request_scope(req).get_required_service(self._endpoints.controller_type)

    async def call_handler_method(self, endpoint: AbstractEndpointDef, controller: TController, req: web.Request):
        args, kwargs = await self.create_args(endpoint, req)
        result = endpoint.controller_method(controller, *args, **kwargs)
        if inspect.isawaitable(result):
            result = await result
        return result

    @staticmethod
    def create_response(endpoint: AbstractEndpointDef, result: Any) -> web.Response:
        return endpoint.signature.serialize_result(result)

    @staticmethod
    def create_error_response(endpoint: AbstractEndpointDef, exception: BaseException) -> web.Response:
        return web.json_response(
            {'error': str(exception)},
            status=http.HTTPStatus.INTERNAL_SERVER_ERROR)

    @staticmethod
    async def create_args(endpoint: AbstractEndpointDef, req: web.Request):
        args, kwargs = [], {}
        await endpoint.signature.deserialize_args(req, args, kwargs)
        return args, kwargs


RouteFactory = Callable[[AbstractEndpointCollection[TController]], Iterable[web.AbstractRouteDef]]


def routes(cls: Type[TController],
           endpoints: AbstractEndpointCollection[TController] | EndpointDefTable,
           factory: RouteFactory[TController] = ControllerRoutes
           ) -> Iterable[web.AbstractRouteDef]:
    """
    Map routes from the controller using default conventions.
    :param cls: the controller class.
    :param endpoints: the controller endpoints.
    :param factory: the mapping that converts endpoints to server routes.
    :return:
    """
    if isinstance(endpoints, EndpointDefTable):
        endpoints = BoundEndpoints(cls, endpoints)
    return factory(endpoints)
