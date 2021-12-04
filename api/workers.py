import requests
import json
import os
from datetime import date

nit_venues =  ["Comerica Center", "UNT Coliseum"]

def update():
	scores = get_scores()
	schedule_to_json(scores)


def get_scores():
	url = "https://sportspage-feeds.p.rapidapi.com/games"

	today = date.today().strftime("%Y-%m-%d")

	querystring = {"league":"ncaab","date":"2021-03-19"}

	try:
		response = requests.request("GET", url, headers=headers, params=querystring)

		return json.loads(response.text)
		
	except ValueError as err:
		print("Something is wrong with the query: {}".format(err))

def schedule_to_json(schedule):
	json_object = []
	if(schedule['status'] == 200 and int(schedule['games']) > 0):
		for game in schedule['results']:
			if(game['venue']['name'] not in nit_venues):
				game_json = {}
				game_json['home_team'] = game['teams']['home']['team']
				game_json['away_team'] = game['teams']['away']['team']
				game_json['ht_abbr'] = game['teams']['home']['abbreviation']
				game_json['spread'] = str(game['odds'][0]['spread']['current']['home'])
				if(game['status'] == 'final'):
					game_json['status'] = 'final'
					game_json['ht_score'] = game['scoreboard']['score']['home']
					game_json['at_score'] = game['scoreboard']['score']['away']
					if(game['scoreboard']['score']['home'] > game['scoreboard']['score']['away']):
						handle_loser(game['teams']['away']['team'])
					else:
						handle_loser(game['teams']['home']['team'])
				else:
					game_json['status'] = 'scheduled'
				json_object.append(game_json)
	if(len(json_object)>0):
		if os.path.exists("./data/schedule.json"):
			os.remove("./data/schedule.json")
		with open("./data/schedule.json", "w") as f:
			json.dump(json_object, f)


def handle_loser(name):
	with open("./data/losers.json", "r") as f:
		json_object = json.load(f)

	if(name not in json_object['losers']):
		json_object['losers'].append(name)
		with open("./data/losers.json", "w") as f:
			json.dump(json_object, f)


def pretty_print(response):
	json_response = json.loads(response.text)

	print(json.dumps(json_response, indent=4, sort_keys=True))

get_scores()
