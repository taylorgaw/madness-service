import json

with open('./data/scheduled_games.json') as f:
	schedule_data = json.load(f)

def add_loser(name):
	with open("./data/losers.json", "r") as f:
		json_object = json.load(f)

	if(name not in json_object['losers']):
		json_object['losers'].append(name)
		with open("./data/losers.json", "w") as f:
			json.dump(json_object, f)


def schedule_to_json(schedule):
	json_object = []
	if(schedule['status'] == 200 and int(schedule['games']) > 0):
		for game in schedule['results']:
			game_json = {}
			game_json['home_team'] = game['teams']['home']['team']
			game_json['away_team'] = game['teams']['away']['team']
			game_json['ht_abbr'] = game['teams']['home']['abbreviation']
			game_json['spread'] = str(game['odds'][0]['spread']['current']['home'])
			if(game['status'] == 'final'):
				game_json['ht_score'] = game['scoreboard']['score']['home']
				game_json['at_score'] = game['scoreboard']['score']['away']
			json_object.append(game_json)
	if(len(json_object)>0):
		#os.remove("./data/schedule.json")
		with open("./data/schedule.json", "w") as f:
			json.dump(json_object, f)

# add_loser("Nebraska")
# add_loser("Wagner")
# add_loser("Wagner")
# add_loser("Yo Mama")

schedule_to_json(schedule_data)