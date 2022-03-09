from flask import Flask, request, jsonify
from flask_cors import CORS

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


@app.route("/health")
def health():
	return "OK"
