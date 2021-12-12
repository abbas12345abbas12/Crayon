r"""
    This is the class that is responsible for handling the HTTP requests. It parses the request and returns it. Is very simple.
    Class that make the magic happen.
"""

import typing

from crayon.config import Config
from crayon.request import Request
from crayon.respone import Respone

class HTTPRequest:
    r"""
        This is the main class to handle the HTTP requests.
    """
    def __init__(
        self,
        config: Config,
        app: typing.Union[typing.Callable,typing.Awaitable]
    ) -> None:
        self.config = config
        self.app = app

    async def __call__(self,scope, recv, send):
        r"""
            This is the main method that is called when the request comes in.
        """
        self.send = send
        self.recv = recv

        body = await self.recv()
        request = Request(scope,body.get('body',b''))

        for middleware in self.config.middlewares:
            respone = await middleware(request)
            if respone:
                await self._send(respone)
                return

        respone = await self.app(request)

        if type(respone) != Respone:
            raise TypeError(f'The app must return an instance of Respone, not ({type(respone).__name__})')

        if respone:
            await self._send(respone)
        else:
            return self._send(Respone(body='No respone',status=404))

    async def _send(self,respone):
        r"""
            This is the main method that is called when the request comes in.
        """
        for dict in respone.to_asgi_response():
            await self.send(dict)

        