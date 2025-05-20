from dataclasses import dataclass, field
from typing import Optional, Protocol, TypeVar, Sequence
from user import User, SupportIdProtocol
from repository import JSONUserRepository
import os, json

USER_ID = "user_id"

class AuthServiceProtocol(Protocol):
    def sign_in(user: User) -> bool:
        ...

    def sign_out(user: User) -> None:
        ...

    @property
    def is_authorized(user: User) -> bool:
        ...
        
    @property
    def current_user(user: User) -> Optional[User]:
        ...


class JSONAuthService(AuthServiceProtocol):
    def __init__(self, repo: JSONUserRepository, auth_file_path: str):
        self.auth_file_path = auth_file_path
        self.repo = repo
        self._current_user: Optional[User] = None
        self._load_session()

    def _load_session(self):
        try:
            with open(self.auth_file_path, 'r') as f:
                session = json.load(f)
                self._current_user = self.repo.get_by_id(session[USER_ID])
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            self._current_user = None # No active session

    def _save_session(self) -> None:
        if not self._current_user:
            return
        try:
            with open(self.auth_file_path, 'w') as file:
                json.dump({USER_ID: self._current_user.id}, file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File wasn't found at {self.auth_file_path}")
        
    def sign_in(self, login: str, password: str) -> bool:
        user = self.repo.get_by_login(login)
        if user and user.password == password:
            self._current_user = user
            self._save_session()
            return True
        return False

    def sign_out(self) -> None:
        self._current_user = None
        try:
            os.remove(self.auth_file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File wasn't found at {self.auth_file_path}")

    @property
    def is_authorized(self) -> bool:
        return self._current_user is not None  # if not authorized, there would be None

    @property
    def current_user(self) -> Optional[User]:
        return self._current_user