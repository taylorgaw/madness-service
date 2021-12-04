from datetime import datetime
from sqlalchemy import Column, Integer, ARRAY, JSON, String, Boolean, inspect 

from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __table_name__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Store as md5 Hash
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    # TODO: color schemes determined by favorite team
    favorite_team = Column(relationship(School, lazy='immediate'))
    theme = Column(String, default='default')
    games = Column(ARRAY, default=[])
    active = Column(Boolean, default=True)

    @classmethod
    def from_dict(cls, d):
        return cls(
            **d
        )

    def to_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }

class GameBoard(Base):
    _table_name_ = 'game_boards'

    id = Column(Integer, primary_key=True)
    # TODO: Create method to generate Default Gameboard Name
    name = Column(String, default = '')
    users = Column(ARRAY, default=[])
    selections = Column(JSON, default={})
    active = Column(Boolean, default=True)
    owner = relationship(User, lazy='immediate')
    created_at = Column(postgresql.TIMESTAMP(timezone=False), nullable=False, default=datetime.utcnow)
    last_updated = Column(postgresql.TIMESTAMP(timezone=False), default=datetime.utcnow)

    @classmethod
    def from_dict(cls, d):
        return cls(
            **d
        )

    def to_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }

class School(Base):
    __table_name__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mascot = Column(String)
    initials = Column(String)

    @classmethod
    def from_dict(cls, d):
        return cls(
            **d
        )

    def to_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }