import re
import json
from contextlib import contextmanager
from typing import Any, Dict, List

from sqlalchemy.sql.expression import false

from db.utils import get_db_session
from db.models import Games, Teams

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
        return session.query(Games).filter(Games.active == True).all()


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


# Teams CRUD methods
def create_teams(teams: Teams) -> int:
    with get_transaction_limited_session(readonly=False) as session:
        session.add(teams)
        session.commit()
        return teams.id


def get_current_teams(year: str = '2022') -> Teams:
    with get_transaction_limited_session() as session:
        return session.query(Teams).filter(Teams.year == year).all()[0]


def update_teams(**updates: Dict[str, Any]) -> None:
    with get_transaction_limited_session(readonly=False) as session:
        session.query(Teams).filter(Teams.id == 1).update(updates)


# Selection Sunday Sync
def update_picks():
    pattern = re.compile('(East|Midwest|West|South) ([1]?[0-9])')

    selections = json.loads(get_current_teams().to_dict()['regions'])
    games = [ game.to_dict() for game in get_all_games() ]
    for game in games:
        picks = game['picks']
        picks_dict = json.loads(picks)
        for pick in picks_dict:
            for key in pick:
                if key != 'user' and key != 'id':
                    value = pick[key]
                    regex_finder = pattern.findall(value)
                    if(regex_finder):
                        region, seed = regex_finder[0]
                        team_name = find_selection(selections, region, seed)
                        pick[key] = team_name
        pick_string = json.dumps(picks_dict)
        update_game(int(game['id']), **{"picks": pick_string})
  

def find_selection(selections, region, seed):
    for group, picks in selections.items():
        if group == region:
            for selection, name in picks.items():
                if selection == seed:
                    return name

    



