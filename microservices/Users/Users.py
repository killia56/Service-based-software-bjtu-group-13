import flask as fl
import sqlite3
import requests
from flask import jsonify
app = fl.Flask(__name__)

def createUser(t):
	conn = sqlite3.connect('Users.db')
	c = conn.cursor()
	c.execute("INSERT INTO users VALUES (?,?)", t)
	conn.commit()

def loginUser(t):
	conn = sqlite3.connect('Users.db')
	c = conn.cursor()
	c.execute('SELECT * FROM users WHERE login=? AND password=?', t)
	return c.fetchone()!=None

def searchUser(t):
	conn = sqlite3.connect('Users.db')
	c = conn.cursor()
	c.execute('SELECT * FROM users WHERE login=?', t)
	return c.fetchone()!=None

def listUser():
	conn = sqlite3.connect('Users.db')
	c = conn.cursor()
	return c.execute('SELECT login FROM users')


@app.route("/", methods=['GET'])
def index():
	return {'message' : 'welcome in Users microservice'}, 200

@app.route("/UsersList", methods=['GET'])
def return_list():
	userlist = []
	for row in listUser():
		userlist.append(row)
	print(userlist)
	return jsonify(userlist), 200

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if fl.request.method == 'POST':
		if not fl.request.form:
			return {'message' : 'body is empty'}, 400
		else:
			password = str(fl.request.form['password'])
			username = str(fl.request.form['username'])
			if not (password and username) :
				return {'message' : 'body require username and password'}, 400
			print(password)
			print(username)
			if searchUser((username,)) == False:
				createUser((username, password,))
			return {'message' : 'user created'}, 200
	else:
		return {'message' : 'signin require POST data'},405

@app.route('/login', methods=['GET', 'POST'])
def login():
	if fl.request.method == 'POST':
		if not fl.request.form:
			return {'message' : 'body is empty'}, 400
		else:
			password = str(fl.request.form['password'])
			username = str(fl.request.form['username'])
			if (not password and username):
				return {'message' : 'body require username and password'}, 400
			print(password)
			print(username)
			res = loginUser((username, password,))
			print(res)
			return {'message' : 'login successfull'}, 200
	else:
		return {'message' : 'login require POST data'}, 405

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)
