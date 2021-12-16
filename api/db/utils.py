'''
Connection functions to create session with db
'''
import json

import mysql.connector

mysql_db = mysql.connector.connect(
        host='mysqldb',
        user='root',
        password='p@ssw0rd1',
        database='madness'
    )

# sqlalchemy.create_engine('mysql+pymysql://root:p@ssw0rd1@mysqldb/madness?charset=utf8mb4')

CREATE_USER_STATEMENT_TEMPLATE = '''INSERT INTO user (name, email, password) VALUES ('{name}', '{email}', '{password}');'''
CREATE_GAME_STATEMENT_TEMPLATE = '''INSERT INTO game (title, owner, picks) VALUES ('{title}', {owner}, '{picks}');'''
CREATE_SCHOOL_STATEMENT_TEMPLATE = '''INSERT INTO school (name, mascot, initials) VALUES ('{name}', '{mascot}', '{initials}');'''
DELETE_STATEMENT_TEMPLATE = '''DELETE FROM {table} WHERE id = {id};'''

# User CRUD methods
def get_all_users():
    cursor = mysql_db.cursor()
    try:
        cursor.execute('SELECT * FROM user;')
        row_headers = [x[0] for x in cursor.description]
        results = cursor.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers, result)))

        cursor.close()

        return json.dumps(json_data, default=str)
    except Exception as e:
        return e.message


def get_user_by_id(id: int):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(f'SELECT * FROM user WHERE id = {id};')
        row_headers = [x[0] for x in cursor.description]
        result = cursor.fetchone()
        cursor.close()
        return dict(zip(row_headers, result))
    except Exception as e: 
        return str(e)


def get_users_by_game_id(game_id: int):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(f'SELECT u.name FROM user_game_match ug JOIN user AS u ON u.id == ug.user_id WHERE ug.user_id = {game_id};')
        # TODO: Figure out how best to return these
        return ''
    except Exception as e:
        return str(e)        


def create_user(name:str, password: str, email: str):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(CREATE_USER_STATEMENT_TEMPLATE.format(name=name, password=password, email=email))
        cursor.close()
    except Exception as e:
        return e


def delete_user_by_id(id: int):
    try:
        cursor = mysql_db.cursor()
        cursor.execute(DELETE_STATEMENT_TEMPLATE.format(table='user', id=id))
        cursor.close()
    except Exception as e:
        return e


# Game CRUD methods
def get_all_games():
    cursor = mysql_db.cursor()
    try:
        cursor.execute('SELECT * FROM game;')
        row_headers = [x[0] for x in cursor.description]
        results = cursor.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers, result)))

        cursor.close()

        return json.dumps(json_data, default=str)
    except Exception as e:
        return e.message


def get_game_by_id(id: int):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(f'SELECT * FROM game WHERE id = {id};')
        row_headers = [x[0] for x in cursor.description]
        result = cursor.fetchone()
        cursor.close()
        return dict(zip(row_headers, result))
    except Exception as e: 
        return str(e)


def get_games_by_user_id(user_id: int):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(f'SELECT g.title FROM user_game_match AS ug JOIN game AS g ON g.id == ug.game_id WHERE ug.user_id = {user_id};')
        # TODO: Figure out how best to return these
    except Exception as e:
        return str(e)


def create_game(title: str, owner: int, picks: dict):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(CREATE_GAME_STATEMENT_TEMPLATE.format(title=title, owner=owner, picks=picks))
    except Exception as e:
        return e


def delete_game_by_id(id: int):
    try:
        cursor = mysql_db.cursor()
        cursor.execute(DELETE_STATEMENT_TEMPLATE.format(table='game', id=id))
        cursor.close()
    except Exception as e:
        return e


# School CRUD methods
def get_all_schools():
    cursor = mysql_db.cursor()
    try:
        cursor.execute('SELECT * FROM school;')
        row_headers = [x[0] for x in cursor.description]
        results = cursor.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers, result)))

        cursor.close()

        return json.dumps(json_data, default=str)
    except Exception as e:
        return e.message


def create_school(name: str, mascot: str, initials: str):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(CREATE_SCHOOL_STATEMENT_TEMPLATE.format(name=name, mascot=mascot, initials=initials))
    except Exception as e:
        return str(e)

def get_school_by_id(id: int):
    cursor = mysql_db.cursor()
    try:
        cursor.execute(f'SELECT * FROM school WHERE id = {id};')
        row_headers = [x[0] for x in cursor.description]
        result = cursor.fetchone()
        cursor.close()
        return dict(zip(row_headers, result))
    except Exception as e: 
        return str(e)


def delete_school_by_id(id: int):
    try:
        cursor = mysql_db.cursor()
        cursor.execute(DELETE_STATEMENT_TEMPLATE.format(table='school', id=id))
        cursor.close()
    except Exception as e:
        return e
