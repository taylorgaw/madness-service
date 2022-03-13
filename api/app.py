from crypt import methods
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sys

import db.madness_repository as db_utils
import db.models as models

app = Flask(__name__)
CORS(app)


# Game Endpoints
@app.route("/games", methods=['GET'])
def get_games():
	games = db_utils.get_all_games()
	return jsonify({"games": [ game.to_dict() for game in games]})


@app.route("/games/<id>", methods=['GET'])
def get_game_by_id(id):
	game = db_utils.get_game_by_id(id)
	if game is None:
		return jsonify({"game":{'title': 'Not Found'}})
	game_dict = game.to_dict()
	tmp = json.loads(game_dict['picks'])
	game_dict['picks'] = tmp
	return jsonify({"game": game_dict})


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
	game_dict = updated_game.to_dict()
	tmp = json.loads(game_dict['picks'])
	game_dict['picks'] = tmp

	return jsonify({"game": game_dict})


@app.route("/games/<id>", methods=['DELETE'])
def delete_game(id):
	game = db_utils.get_game_by_id(id)
	if not game:
		return {'Error' : 'Game with id {id} does not exist'}

	db_utils.delete_game_by_id(game.id)
	return { 'status': 'Success!' }


@app.route("/games/update", methods=['PUT'])
def update_picks():
	try: 
		db_utils.update_picks()
		return { 'status': 'Success!'}
	except TypeError as e:
		e = sys.exc_info()[2]
		return { 'status': f'Failed! {str(e.print_exception())}' }


@app.route("/teams", methods=['POST'])
def create_teams():
	body = request.get_json()
	game_model = models.Teams.from_dict(body)
	game_id = db_utils.create_teams(game_model)

	return str({'id': game_id})

@app.route("/teams", methods=['GET'])
def get_teams():
	teams = db_utils.get_current_teams()
	
	teams_dict = teams.to_dict()
	tmp = json.loads(teams_dict['regions'])
	teams_dict['regions'] = tmp
	return jsonify(teams_dict)
	

@app.route("/teams", methods=['PUT'])
def update_teams():
	body = request.get_json()
	db_utils.update_teams(**body)

	updated_teams = db_utils.get_current_teams()
	teams_dict = updated_teams.to_dict()
	tmp = json.loads(teams_dict['regions'])
	teams_dict['regions'] = tmp

	return jsonify(teams_dict)


@app.route("/health")
def health():
	return "OK"
