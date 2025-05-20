from repository_protocols import DataRepositoryProtocol, UserRepositoryProtocol
from typing import TypeVar, Optional, Sequence
from user import User
import os, json

T = TypeVar('T')

ID = "id" # just to easily override
LOGIN = "login"

class JSONDataRepository(DataRepositoryProtocol[T]):
    def __init__(self, file_path: str, T: type):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            self.file_path = file_path
            self._data = self._load_data()
            self.T = T
        except (FileNotFoundError, json.JSONDecodeError) as error:
            #print(error, self.file_path, sep="\n")
            raise error
        
    # region save/load

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            #print(error, self.file_path, sep="\n")
            raise error

    def _save_data(self) -> None:
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self._data, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            #print(error, self.file_path, sep="\n")
            raise error
        
    # endregion

    # region CRUD
        
    # Conversion from JSON data to T: T(**item), where **item - kwargs from item

    def get_all(self) -> Sequence[T]:
        return [self.T(**item) for item in self._load_data()]

    def get_by_id(self, id: int) -> Optional[T]:
        for item in self._load_data():
            if item[ID] == id:
                return self.T(**item)
        return None

    def add(self, item: T) -> None:
        self._data.append(item.__dict__) # Convert from T to JSON item
        self._save_data()

    def update(self, item: T) -> None:
        for index, entry in enumerate(self._data):
            if entry[ID] == item.id:
                self._data[index] = item.__dict__
                break
        self._save_data()

    def delete(self, item: T) -> None:
        try:
            self._data.remove(item.__dict__)
            self._save_data()
        except ValueError:
            pass # Item just isn't in repo, no actions needed

    # endregion

class JSONUserRepository(JSONDataRepository[User], UserRepositoryProtocol):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path, T=User)

    def get_by_login(self, login: str) -> Optional[User]:
        for item in self._load_data():
            if item[LOGIN] == login:
                return User(**item)
        return None