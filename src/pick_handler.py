import json


with open('./data/picks.json') as f:
	loser_data = json.load(f)

def picks_to_html(picks):