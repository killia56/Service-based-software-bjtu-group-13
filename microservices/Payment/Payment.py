import flask as fl
import sqlite3
import requests
conn = sqlite3.connect('ticket.db')
c = conn.cursor()

app = fl.Flask(__name__)

def createTicket(t):
	conn = sqlite3.connect('ticket.db')
	c = conn.cursor()
	c.execute("INSERT INTO tickets VALUES (?,?,0)", t)
	conn.commit()

def ticketPaid(t):
	conn = sqlite3.connect('ticket.db')
	c = conn.cursor()
	c.execute('SELECT * FROM tickets WHERE user = ? AND movie=?', t)
	tmp = c.fetchone()
	c.execute('UPDATE tickets SET paid = 1 WHERE user=? AND movie = ?', t)
	conn.commit()
	return tmp[2]==0

def searchTicket(t):
	conn = sqlite3.connect('ticket.db')
	c = conn.cursor()
	c.execute('SELECT * FROM tickets WHERE user = ? AND movie=?', t)
	return c.fetchone()!=None

def allTickets():
	conn = sqlite3.connect('ticket.db')
	c = conn.cursor()
	return c.execute('SELECT * FROM tickets')

@app.route("/", methods=['GET'])
def index():
	return "P"

@app.route('/createTicket/', methods=['GET', 'POST'])
def creationTicket(username, movie):
	if fl.request.method == 'POST':
		if not fl.request.form:
			return "False"
		else:
			username = str(fl.request.form['username'])
			movie = str(fl.request.form['movie'])
			if not username or movie:
				return "False"
			if searchTicket((username, movie,)) == False:
				createTicket((username, movie,))
				return "OK"
			else:
				return "KO"

@app.route('/confirmation/')
def confirmed(username, movie):
	if fl.request.method == "POST":
		if not fl.request.form:
			return "False"
		else:
			username = str(fl.request.form['username'])
			movie = str(fl.request.form['movie'])
			if not username or movie:
				return "False"
				ticketPaid((username, movie,))
				return "Done"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5003, debug=True)