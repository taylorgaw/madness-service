from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, inspect 

from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Games(Base):
    __tablename__ = 'games'

    def __repr__(self):
        return str(self.to_dict())

    id = Column(Integer, primary_key=True)
    title = Column(String, default = '')
    picks = Column(String, default='[\{\}]')
    active = Column(Boolean, default=True)
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


class Teams(Base):
    __tablename__ = 'teams'

    def __repr__(self):
        return str(self.to_dict())

    id = Column(Integer, primary_key=True)
    year = Column(String, default = '')
    regions = Column(String, default='\{\}')
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
