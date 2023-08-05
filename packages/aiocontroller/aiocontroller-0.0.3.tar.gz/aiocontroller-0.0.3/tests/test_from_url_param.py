from aiocontroller import EndpointDefTable, client_factory
from aiocontroller.endpoints import FromUrl


def test_read_param():
    endpoints = EndpointDefTable()
    route_path = '/api/{arg}'

    class Controller:
        @endpoints.get(route_path)
        def handler(arg: int) -> None:
            pass

    endpoint = endpoints[Controller.handler]

    assert endpoint.route_path == route_path
    assert endpoint.controller_method == Controller.handler

    arg_param = endpoint.signature.params[0]
    assert isinstance(arg_param, FromUrl)
    assert arg_param.payload_name == 'arg'

    new_client = client_factory(Controller, endpoints)
    req = new_client.build_request(endpoint, [1], {})
    assert req.url_params['arg'] == '1'
    assert req.route == '/api/1'
