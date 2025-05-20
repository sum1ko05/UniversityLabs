from dataclasses import dataclass, field
from typing import Optional, Protocol, Self


class SupportIdProtocol(Protocol):
    id: int


@dataclass
class User:
    id: int = field(init=True)  # cwinge typing >w<
    login: str = field(init=True)
    password: str = field(repr=False, compare=False)  # repr is set to False to not show this field on repr()
    name: str = field(compare=False)
    email: Optional[str] = field(default=None, compare=False)
    address: Optional[str] = field(default=None, compare=False)

    def __gt__(self, other: Self):
        return self.name.upper() > other.name.upper()
    
    def __lt__(self, other: Self):
        return self.name.upper() < other.name.upper()