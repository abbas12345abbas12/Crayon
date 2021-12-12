r"""
    Configuration class for Cryon handlers. This is just a class to contain the configuration 
"""

import dataclasses
import typing

@dataclasses.dataclass(
    init=True
)
class Config:
    def __init__(
        self,
        *,
        middlewares:typing.List[typing.Union[typing.Callable,typing.Awaitable]] = [],
        encoding:str = 'utf-8',
    ) -> None:
        self.middlewares = middlewares
        self.encoding = encoding

    def __repr__(self) -> str:
        return (
            f'<Config encoding={self.encoding}>'
        )