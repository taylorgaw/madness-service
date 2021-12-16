import json

from flask import Flask, request
from sqlalchemy.sql.sqltypes import Date

import db.utils as db_utils

app = Flask(__name__)

  
@app.route("/")
def hello_world():
	return "OK"


#User Endpoints
@app.route("/users", methods=['GET'])
def get_users():
	results = db_utils.get_all_users()
	if results:
		return results
	else:
		return 'Success!'


@app.route("/user", methods=['GET'])
def get_user_by_id():
	data = request.get_json()

	result = db_utils.get_user_by_id(data['id'])
	
	if result:
		return result
	else:
		return 'Success!'


@app.route("/users/game", methods=['GET'])
def get_users_by_game_id():
	data = request.get_json()

	result = db_utils.get_users_by_game_id(data['id'])
	
	if result:
		return result
	else:
		return 'Success!'


@app.route("/users", methods=['POST'])
def create_user():
	data = request.get_json()

	result = db_utils.create_user(data['name'], data['email'], data['password'])

	if result:
		return result
	else:
		return 'Success!'


@app.route("/users", methods=['DELETE'])
def delete_user():
	data = request.get_json()
	
	result = db_utils.delete_user_by_id(data['id'])

	if result:
		return result
	else:
		return 'Success!'


# Game Endpoints
@app.route("/games", methods=['GET'])
def get_games():
	results = db_utils.get_all_users()
	if results:
		return results
	else:
		return 'Success!'


@app.route("/game", methods=['GET'])
def get_game_by_id():
	data = request.get_json()

	result = db_utils.get_game_by_id(data['id'])
	
	if result:
		return result
	else:
		return 'Success!'

@app.route("/games/user", methods=['GET'])
def get_games_by_user_id():
	data = request.get_json()

	results = db_utils.get_games_by_user_id(data['id'])

	if results:
		return results
	else:
		return 'Success!'


@app.route("/games", methods=['POST'])
def create_game():
	data = request.get_json()

	# TODO replace with generate_game_board method
	picks = {}
	result = db_utils.create_game(data['title'], data['owner'], picks)

	if result:
		return result
	else:
		return 'Success!'


@app.route("/games", methods=['DELETE'])
def delete_game():
	data = request.get_json()
	
	result = db_utils.delete_game_by_id(data['id'])

	if result:
		return result
	else:
		return 'Success!'		


# School CRUD
@app.route("/schools", methods=['GET'])
def get_schools():
	results = db_utils.get_all_schools()
	if results:
		return results
	else:
		return 'Success!'


@app.route("/school", methods=['GET'])
def get_school_by_id():
	data = request.get_json()

	result = db_utils.get_school_by_id(data['id'])
	
	if result:
		return result
	else:
		return 'Success!'


@app.route("/schools", methods=['POST'])
def create_school():
	data = request.get_json()

	result = db_utils.create_school(data['name'], data['mascot'], data['initials'])

	if result:
		return result
	else:
		return 'Success!'


@app.route("/schools", methods=['DELETE'])
def delete_schools():
	data = request.get_json()
	
	result = db_utils.delete_school_by_id(data['id'])

	if result:
		return result
	else:
		return 'Success!'

if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug=True)
