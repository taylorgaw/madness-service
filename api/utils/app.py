import json

import mysql.connector
from flask import Flask

app = Flask(__name__)

  
@app.route("/")
def hello_world():
	return "Hello World!"


@app.route("/games")
def get_games():
	my_db = mysql.connector.connect(
		host='mysqldb',
		user='root',
		password='p@ssw0rd1',
		database='madness'
	)
	cursor = my_db.cursor()

	cursor.execute('SELECT * FROM game')

	row_headers = [x[0] for x in cursor.description]

	results = cursor.fetchall()
	json_data = []
	for result in results:
		json_data.append(dict(zip(row_headers, result)))

	cursor.close()

	return json.dumps(json_data, default=str)


@app.route("/users")
def get_users():
	my_db = mysql.connector.connect(
		host='mysqldb',
		user='root',
		password='p@ssw0rd1',
		database='madness'
	)
	cursor = my_db.cursor()

	cursor.execute('SELECT * FROM user')

	row_headers = [x[0] for x in cursor.description]

	results = cursor.fetchall()
	json_data = []
	for result in results:
		json_data.append(dict(zip(row_headers, result)))

	cursor.close()

	return json.dumps(json_data, default=str)


if __name__ == "__main__":
  app.run(host ='0.0.0.0')
