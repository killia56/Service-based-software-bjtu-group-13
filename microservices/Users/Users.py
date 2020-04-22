import flask as fl
import sqlite3
import requests
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

@app.route("/", methods=['GET'])
def index():
	return "U"

@app.route('/signin/<username>/<password>', methods=['GET', 'POST'])
def signin(username, password):
	if searchUser((username,)) == False:
		createUser((username, password,))
	rep = str(fl.request.data)
	return "True"

@app.route('/login/<username>/<password>', methods=['GET', 'POST'])
def login(username, password):
	rep = str(fl.request.data)
	res = loginUser((username, password,))
	print(res)
	return "OK"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)

conn.close()
	