import flask as fl
import sqlite3 as sql
import requests

app = fl.Flask(__name__)


@app.route("/", methods=['GET'])
def index():
	return ""


if __name__ == '__main__':
	app.run(host='localhost', port=5003, debug=True)