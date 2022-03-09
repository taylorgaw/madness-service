from contextlib import contextmanager
from typing import Any, Dict, List

from sqlalchemy.sql.expression import false

from db.utils import get_db_session
from db.models import Games

# Update Game

CREATE_GAME_STATEMENT_TEMPLATE = '''INSERT INTO games (title, owner, picks) VALUES ('{title}', {owner}, '{picks}');'''
DELETE_STATEMENT_TEMPLATE = '''DELETE FROM {table} WHERE id = {id};'''

@contextmanager
def get_transaction_limited_session(readonly: bool=True):
    session = get_db_session()
    try:
        yield session
        if not readonly:
            session.commit()
    except:
        if not readonly:
            session.rollback()
        raise
    finally:
        session.close()


# Game CRUD methods
def create_game(game: Games) -> int:
    with get_transaction_limited_session(readonly=False) as session:
        session.add(game)
        session.commit()
        return game.id


def get_all_games() -> List[Games]:
    with get_transaction_limited_session() as session:
        return session.query(Games).all()


def get_game_by_id(game_id: int) -> Games:
    with get_transaction_limited_session() as session:
        return session.query(Games).get({'id': game_id})


def update_game(game_id: int, **updates: Dict[str, Any]) -> None:
    with get_transaction_limited_session(readonly=False) as session:
        session.query(Games).filter(Games.id == game_id).update(updates)


def delete_game_by_id(game_id: int):
    with get_transaction_limited_session(readonly=False) as session:
        session.query(Games).filter(
            Games.id == game_id
        ).update({"active": False})
