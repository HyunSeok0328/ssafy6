from _typeshed import IdentityFunction
from typing import Callable, Optional, Sequence, TypeVar

_T = TypeVar("_T")

def lfu_cache(maxsize: float = ..., typed: bool = ...) -> IdentityFunction: ...
def lru_cache(maxsize: float = ..., typed: bool = ...) -> IdentityFunction: ...
def rr_cache(
    maxsize: float = ..., choice: Optional[Callable[[Sequence[_T]], _T]] = ..., typed: bool = ...
) -> IdentityFunction: ...
def ttl_cache(maxsize: float = ..., ttl: float = ..., timer: float = ..., typed: bool = ...) -> IdentityFunction: ...