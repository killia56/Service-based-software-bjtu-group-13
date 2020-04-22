import flask as fl
import sqlite3 as sql
import requests

app = fl.Flask(__name__)


@app.route("/", methods=['GET'])
def index():
	return "U"

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	print(str(fl.request.data))
	return True

@app.route('/login', methods=['GET', 'POST'])
def login():
	print(str(fl.request.data))
	return True

@app.route("/users/<username>/bookings", methods=['GET'])
def user_bookings(username):
	try:
		users_bookings = requests.get("http://127.0.0.1:5002/bookings/"+username)
	except requests.exceptions.ConnectionError:
		return("The Bookings service is unavailable.")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)
	