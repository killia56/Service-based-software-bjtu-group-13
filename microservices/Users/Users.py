import flask as fl
import sqlite3
import requests
conn = sqlite3.connect('Users.db')
c = conn.cursor()
app = fl.Flask(__name__)

def createUser(t):
	c.execute("INSERT INTO users VALUES (?,?)", t)
	conn.commit()

def loginUser(t):
	c.execute('SELECT * FROM users WHERE login=? AND password=?', t)
	return c.fetchone()!=None

def searchUser(t):
	c.execute('SELECT * FROM users WHERE login=?', t)
	return c.fetchone()!=None

@app.route("/", methods=['GET'])
def index():
	return "U"

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	rep = str(fl.request.data)
	return True

@app.route('/login', methods=['GET', 'POST'])
def login():
	rep = str(fl.request.data)
	print("lol",rep)
	return "True"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)
	