import json
import os

nit_venues =  ["Comerica Center", "UNT Coliseum"]

with open('./data/final_games.json') as f:
	schedule_data = json.load(f)

with open('./data/final_games.json') as f:
	result_data = json.load(f)

with open('./data/losers.json') as f:
	loser_data = json.load(f)

def print_schedule(schedule):
	for game in schedule:
		if(game['venue']['name'] not in nit_venues):
			ht = game['teams']['home']['team']
			at = game['teams']['away']['team']
			if(game['status'] != 'final'):
				ht_abbr = game['teams']['home']['abbreviation']
				spread = str(game['odds'][0]['spread']['current']['home'])
				if(spread[0] != '-'):
					spread = "+" + spread
				print("Home Team: {}".format(ht))
				print("Away Team: {}".format(at))
				print("Spread: {} {}".format(ht_abbr, spread))
				print()
			else:
				winner, loser = calculate_winner(game)
				print("Winner: {} {}".format(winner[0], winner[1]))
				print("Loser: {} {}".format(loser[0], loser[1]))
				print()


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
				game_json['status'] = 'final'
				game_json['ht_score'] = game['scoreboard']['score']['home']
				game_json['at_score'] = game['scoreboard']['score']['away']
			else:
				game_json['status'] = 'scheduled'
			json_object.append(game_json)
	if(len(json_object)>0):
		if os.path.exists("./data/schedule.json"):
			os.remove("./data/schedule.json")
		with open("./data/schedule.json", "w") as f:
			json.dump(json_object, f)
	print("Done!")


def calculate_winner(game):
	home_team = game['teams']['home']['team']
	away_team = game['teams']['away']['team']
	ht_score = game['scoreboard']['score']['home']
	at_score = game['scoreboard']['score']['away']
	if(ht_score > at_score):
		handle_loser(away_team)
		return ((home_team, ht_score), (away_team, at_score))
	else:
		handle_loser(home_team)		
		return ((away_team, at_score), (home_team, ht_score))


def handle_loser(name):
	with open("./data/losers.json", "r") as f:
		json_object = json.load(f)

	if(name not in json_object['losers']):
		json_object['losers'].append(name)
		with open("./data/losers.json", "w") as f:
			json.dump(json_object, f)



if(schedule_data['status'] == 200 and int(schedule_data['games']) > 0):
	schedule_to_json(schedule_data)
	#print_results(result_data['results'])

