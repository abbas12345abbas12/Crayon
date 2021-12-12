r"""
    The request module contains the Request class, which is used to represent the request data.
"""

import dataclasses
import typing

from urllib.parse import parse_qsl
from yarl import URL

@dataclasses.dataclass(repr=True)
class Request:
    encoding:str='utf-8'
    """
        The Request class is used to represent the request data.
    """
    def __init__(
        self,
        scope:typing.Dict,
        body:typing.Dict[str,typing.Any]
    ) -> None:
        self.scope = scope
        self.body = body

    @property
    def url(self) -> URL:
        """
            Returns the url of the request.
        """
        return URL(self.scope['path'])

    @property
    def headers(self) -> typing.Dict:
        """
            Returns the headers of the request.
        """
        return dict( (key.decode(self.encoding),value.decode(self.encoding)) for key,value in self.scope['headers'] )

    @property
    def text(self) -> str:
        """
            Returns the body of the request as text.
        """
        return self.body.decode('utf-8')

    @property
    def method(self):
        """
            Returns the method of the request.
        """
        return self.scope['method']

    @property
    def query(self) -> typing.Dict:
        """
            Returns the query of the request.
        """
        return parse_qsl(self.scope['query_string'])

    @property
    def version(self):
        """
            Returns the version of the request.
        """
        return self.scope['http_version']

    def __repr__(self) -> str:
        return (
            f"<Request path='{self.url.raw_path}' method='{self.method}'>"
        )