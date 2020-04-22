import flask as fl
import sqlite3 as sql
import requests

app = fl.Flask(__name__)


@app.route("/", methods=['GET'])
def index():
	return ""


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=True)