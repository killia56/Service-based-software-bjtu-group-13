import flask as fl
import sqlite3
import requests


app = fl.Flask(__name__)

def searchMovie(t):
	conn = sqlite3.connect('Ticket.db')
	c = conn.cursor()
	c.execute('SELECT * FROM movies WHERE movie=?', t)
	return c.fetchone()!=None
	conn.commit()

def createMovie(t):
	conn = sqlite3.connect('Ticket.db')
	c = conn.cursor()
	c.execute("INSERT INTO movies VALUES (?,?,?)", t)
	conn.commit()

def allMovies():
	conn = sqlite3.connect('Ticket.db')
	c = conn.cursor()
	return c.execute('SELECT * FROM movies')

def buySeat(t):
	conn = sqlite3.connect('Ticket.db')
	c = conn.cursor()
	c.execute('SELECT * FROM movies WHERE movie=?', t)
	tmp = c.fetchone()
	# print("seat bought for " + tmp[0] + " : " + str(tmp[2]) + "/" + str(tmp[1]) + " Success to bought : " + str(tmp[2] < tmp[1]))
	c.execute('UPDATE movies SET seatBought = seatBought + 1 WHERE movie=? AND seatBought < seat', t)
	conn.commit()
	return tmp[2] < tmp[1]

@app.route("/", methods=['GET'])
def index():

	return "T"

@app.route('/createMovie/', methods=['GET', 'POST'])
def movieCreation(movieName, seatnb, soldnb):
	if fl.request.method == 'POST':
		if not fl.request.form:
			return "False"
		else:
			movieName = str(fl.request.form['movieName'])
			seatnb = str(fl.request.form['seatnb'])
			soldnb = str(fl.request.form['soldnb'])
			if not movieName or seatnb or soldnb:
				return "False"
			if searchMovie((movieName,)) == False:
				createMovie((movieName, seatnb, soldnb))
				return "True"

@app.route('/buySeat/', methods=['GET', 'POST'])
def seat(movie):
	if fl.request.method == 'POST':
		if not fl.request.form:
			return "False"
		else:
			movie = str(fl.request.form['movie'])
			if not movie:
				return "False"
			if buySeat((movie,)) == True:
				return "OK"
			else :
				return "KO"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=True)