r"""
    The servering module. This module is responsible for serving the http/websocket and handling the requests.
"""
import typing

from crayon.config import Config
from crayon.http import HTTPRequest

def asgi_applications(config:Config=Config()):
    r"""
        This function returns a function of asgi applications.
    """
    def deco(func:typing.Union[typing.Awaitable,typing.Callable]):
        r"""
            This is the decorator for the asgi applications.
        """
        async def wrapper(scope:typing.Dict[str,typing.Any], receive:typing.Callable, send:typing.Callable):
            r"""
                This is the wrapper for the asgi applications.
            """
            if scope["type"] == "http":
                await HTTPRequest(config,func).__call__(scope, receive, send)
        return wrapper
    return deco

def to_asgi(func:typing.Union[typing.Awaitable,typing.Callable],config:Config):
    """
        This is an alternative to the make asgi_application without using the decorator.
    """
    @asgi_applications(config)
    async def wrapper(request):
        return await func(request)
    return wrapper