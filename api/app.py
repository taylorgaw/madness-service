from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import db.madness_repository as db_utils
import db.models as models
from endpoint_models import GameRequest

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
	return "OK"


# Game Endpoints
# TODO: This is all very broken
@app.route("/games", methods=['GET'])
def get_games():
	games = db_utils.get_all_games()
	return jsonify({"games": [ game.to_dict() for game in games]})


@app.route("/games/<id>", methods=['GET'])
def get_game_by_id(id):
	game = db_utils.get_game_by_id(id)
	return jsonify({"game":game.to_dict()})


@app.route("/games", methods=['POST'])
def create_game():
	body = request.get_json()
	game_model = models.Games.from_dict(body)
	game_id = db_utils.create_game(game_model)

	return str({'id': game_id})


@app.route("/games/<id>", methods=['PUT'])
def update_game(id):
	body = request.get_json()
	game = db_utils.get_game_by_id(id)
	if not game:
		return {'Error' : 'Game with id {id} does not exist'}

	db_utils.update_game(game.id, **body)
	updated_game = db_utils.get_game_by_id(id)
	return jsonify({"game":updated_game.to_dict()})


@app.route("/games/<id>", methods=['DELETE'])
def delete_game(id):
	game = db_utils.get_game_by_id(id)
	if not game:
		return {'Error' : 'Game with id {id} does not exist'}

	db_utils.delete_game_by_id(game.id)
	return { 'status': 'Success!' }


# @app.route("/games/user/{id}", methods=['GET'])
# def get_games_by_user_id(id):
# 	results = db_utils.get_games_by_user_id(id)

# 	if results:
# 		return results
# 	else:
# 		return 'Success!'


# #User Endpoints
# @app.route("/users", methods=['GET'])
# def get_users():
# 	results = db_utils.get_all_users()
# 	return str(results)


# @app.route("/users/<id>", methods=['GET'])
# def get_user_by_id(id):
# 	results = db_utils.get_user_by_id(id)
# 	return str(results.to_dict())


# @app.route("/users", methods=['POST'])
# def create_user():
# 	body = request.get_json()
# 	user_request = UserRequest.from_dict(body)
# 	user_model = user_request.to_db_model()
# 	user_id = db_utils.create_user(user_model)

# 	return str({'id': user_id})


# #TODO: Update isn't committing to DB
# @app.route("/users", methods=['PUT'])
# def update_user():
# 	body = request.get_json()
# 	try:
# 		user = db_utils.get_user_by_id(body['id'])
# 	except Exception as e:
# 		return 'User does not exist'
# 	user_request = UserRequest.from_dict(body)
# 	#user_model = user_request.to_db_model()
# 	return str(db_utils.update_user(user.id, **user_request.to_update_dict()))


# @app.route("/users", methods=['DELETE'])
# def delete_user():
# 	data = request.get_json()
# 	try:
# 		user = db_utils.get_user_by_id(data['id'])
# 	except:
# 		return f'Error: User with id {data["id"]} does not exist'

# 	db_utils.delete_user_by_id(user.id)
# 	return 'Success!'


# @app.route("/users/games/{id}", methods=['GET'])
# def get_users_by_game_id(id):
# 	result = db_utils.get_users_by_game_id(id)
# 	return result


# # School CRUD
# @app.route("/schools", methods=['GET'])
# def get_schools():
# 	results = db_utils.get_all_schools()
# 	if results:
# 		return results
# 	else:
# 		return 'Success!'


# @app.route("/school", methods=['GET'])
# def get_school_by_id():
# 	data = request.get_json()

# 	result = db_utils.get_school_by_id(data['id'])
	
# 	if result:
# 		return result
# 	else:
# 		return 'Success!'


# @app.route("/schools", methods=['POST'])
# def create_school():
# 	data = request.get_json()

# 	result = db_utils.create_school(data['name'], data['mascot'], data['initials'])

# 	if result:
# 		return result
# 	else:
# 		return 'Success!'


# @app.route("/schools", methods=['DELETE'])
# def delete_schools():
# 	data = request.get_json()
	
# 	result = db_utils.delete_school_by_id(data['id'])

# 	if result:
# 		return result
# 	else:
# 		return 'Success!'
