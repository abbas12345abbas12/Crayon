r"""
    This module contains the Response class. This is just a warrper for the ASGI respone object.
"""
import dataclasses
import typing

@dataclasses.dataclass(repr=True)
class Respone:
    encoding:str='utf-8'
    def __init__(
        self,
        body:str,
        status:int=200,
        mimetype:str="text/html",
        headers:typing.Dict[str,str]={},
    ) -> None:
        self.body = body
        self.status = status
        self.mimitype = mimetype
        self.headers = headers

        self.headers['Content-Type'] = self.mimitype

    def add_header(self,key:str,value:str) -> None:
        """
            Add a header to the response.
        """
        self.headers[key] = value

    def to_asgi_response(self):
        return [
            {
                'type'    : 'http.response.start',
                'status'  : self.status,
                'headers' : [(key.encode(self.encoding),value.encode(self.encoding),) for key,value in self.headers.items()],
            },
            {
                'type': 'http.response.body',
                'body': self.body.encode(self.encoding)
            }
        ]

    def __repr__(self) -> str:
        return f"<Response status='{self.status}' mimitype='{self.mimitype}'>"