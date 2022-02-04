import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
import yaml
from yaml.loader import Loader


CONNECTION_STRING = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'


def get_db_creds() -> dict:
    with open('conf.yaml') as f:
        config = yaml.load(f, Loader=Loader)['mysql']
        return config


def _get_engine_from_creds(creds: dict):
    return sqlalchemy.create_engine(
        CONNECTION_STRING.format(
            user=creds['user'], 
            password=creds['password'], 
            host=creds['host'], 
            database=creds['db']
        )
    )


def _get_session_from_creds(creds: dict):
    engine = _get_engine_from_creds(creds)

    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    return Session()


def get_db_session():
    db_creds = get_db_creds()
    return _get_session_from_creds(db_creds)
