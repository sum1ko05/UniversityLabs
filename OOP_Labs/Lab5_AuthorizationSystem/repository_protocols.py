from dataclasses import dataclass, field
from typing import Optional, Protocol, TypeVar, Sequence
from user import User, SupportIdProtocol

T = TypeVar('T')

class DataRepositoryProtocol(Protocol[T]):
    def get_all(self) -> Sequence[T]:
        ...

    def get_by_id(self, id: int) -> Optional[T]:
        ...

    def add(self, item: T) -> None:
        ...

    def update(self, item:T ) -> None:
        ...

    def delete(self, item: T) -> None:
        ...

class UserRepositoryProtocol(DataRepositoryProtocol[User], Protocol):
    def get_by_login(self, login: str) -> Optional[User]:
        ...