from copy import copy
from dataclasses import dataclass
from typing import Any, Dict
import json

from sqlalchemy.sql.sqltypes import JSON

from db.models import (
    Games
)

class RequestValidationError(Exception):
    pass



@dataclass
class GameRequest():
    #required fields
    title = str
    owner = int
    picks = str
    active = bool


    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'GameRequest':
        dict_for_init = copy(d)
        return cls(**dict_for_init)

    def to_db_model(self) -> Games:
        return Games(
            title=self.title,
            owner=self.owner,
            picks=json.dumps(self.picks),
            active=self.active
        )

    def to_update_dict(self):
        update_dict = self.to_db_model().to_dict()
        del update_dict['last_updated']
        del update_dict['created_at']

        return update_dict


# @dataclass
# class UserRequest():
#     #required fields
#     name: str
#     username: str
#     email: str
#     password: str
#     # ID is required for PUT requests
#     id: Optional[int] = None
#     admin: bool = False


#     @classmethod
#     def from_dict(cls, d) -> 'UserRequest':
#         dict_for_init = copy(d)
#         return cls(**dict_for_init)

#     def to_db_model(self) -> Users:
#         return Users(
#             id=self.id,
#             name=self.name,
#             username=self.username,
#             email=self.email,
#             password=self.password,
#             admin=self.admin
#         )

#     def to_update_dict(self):
#         update_dict = self.to_db_model().to_dict()
#         del update_dict['last_updated']
#         del update_dict['created_at']

#         return update_dict
