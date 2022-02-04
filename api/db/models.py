from datetime import datetime
from sqlalchemy import Column, Integer, ARRAY, JSON, String, Boolean, inspect 

from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    def __repr__(self):
        return str(self.to_dict())

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    # Store as md5 Hash
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    created_at = Column(postgresql.TIMESTAMP(timezone=False), nullable=False, default=datetime.utcnow)
    last_updated = Column(postgresql.TIMESTAMP(timezone=False), default=datetime.utcnow)    
    # TODO: color schemes determined by favorite team
    # favorite_team = Column(relationship(School, lazy='immediate'))
    # theme = Column(String, default='default')
    # active = Column(Boolean, default=True)

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

class Games(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    # TODO: Create method to generate Default Gameboard Name
    title = Column(String, default = '')
    picks = Column(String, default={})
    active = Column(Boolean, default=True)
    owner = Column(ForeignKey(Users.id))
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

class Schools(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mascot = Column(String)
    initials = Column(String)
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