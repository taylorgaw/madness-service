from contextlib import contextmanager
from typing import Any, Dict, List

from sqlalchemy.sql.expression import false

from db.utils import get_db_session
from db.models import Users, Games, Schools

# Update Users
# Switch User active to False
# Update Game
# Switch Game Active to False

CREATE_USER_STATEMENT_TEMPLATE = '''INSERT INTO users (name, email, password) VALUES ('{name}', '{email}', '{password}');'''
CREATE_GAME_STATEMENT_TEMPLATE = '''INSERT INTO games (title, owner, picks) VALUES ('{title}', {owner}, '{picks}');'''
CREATE_SCHOOL_STATEMENT_TEMPLATE = '''INSERT INTO schools (name, mascot, initials) VALUES ('{name}', '{mascot}', '{initials}');'''
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


# def get_games_by_user_id(user_id: int)  -> List[models.Game]:
#     cursor = mysql_db.cursor()
#     try:
#         cursor.execute(f'SELECT g.title FROM user_game_match AS ug JOIN game AS g ON g.id == ug.game_id WHERE ug.user_id = {user_id};')
#         # TODO: Figure out how best to return these
#     except Exception as e:
#         return str(e)


def delete_game_by_id(game_id: int):
    with get_transaction_limited_session(readonly=False) as session:
        session.query(Games).filter(
            Games.id == game_id
        ).delete()


# User CRUD methods
def get_all_users() -> List[Users]:
    with get_transaction_limited_session() as session:
        return session.query(Users).all()
    

def get_user_by_id(user_id: int) -> Users:
    with get_transaction_limited_session() as session:
        return session.query(Users).get({'id': user_id})


# def get_users_by_game_id(game_id: int) -> List[models.User]:
#     cursor = mysql_db.cursor()
#     try:
#         cursor.execute(f'SELECT u.name FROM user_game_match ug JOIN user AS u ON u.id == ug.user_id WHERE ug.user_id = {game_id};')
#         # TODO: Figure out how best to return these
#         return ''
#     except Exception as e:
#         return str(e)        


def create_user(user: Users) -> int:
    with get_transaction_limited_session(readonly=False) as session:
        session.add(user)

    return user.id


def update_user(user_id: int, **updates: Dict[str, Any]) -> None:
    with get_transaction_limited_session(readonly=False) as session:
        session.query(Users).filter(Users.id == user_id).update(updates)


def delete_user_by_id(user_id: int) -> None:
    with get_transaction_limited_session(readonly=False) as session:
        session.query(Users).filter(
            Users.id == user_id
        ).delete()


# School CRUD methods
def get_all_schools() -> List[Schools]:
    with get_transaction_limited_session() as session:
        return session.query(Schools).all()


def create_school(school: Schools) -> int:
    with get_transaction_limited_session(readonly=False) as session:
        session.add(school)

    return school.id


def get_school_by_id(school_id: int) -> Schools:
    with get_transaction_limited_session() as session:
        session.query(Schools).get({'id': school_id})


def update_school(school_id: int, **updates: Dict[str, Any]):
    with get_transaction_limited_session(readonly=False) as session:
        session.query(Schools).filter(Schools.id == school_id).update(updates)


def delete_school_by_id(school_id: int):
    with get_transaction_limited_session(readonly=False) as session:
            session.query(Schools).filter(
                Schools.id == school_id
            ).delete()
