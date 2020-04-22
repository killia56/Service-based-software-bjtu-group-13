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

@app.route('/createMovie/<movieName>/<seatnb>/<soldnb>', methods=['GET', 'POST'])
def movieCreation(movieName, seatnb, soldnb):
	if searchMovie((movieName,)) == False:
		createMovie((movieName, seatnb, soldnb))
	rep = str(fl.request.data)
	return "True"

@app.route('/buySeat/<movie>', methods=['GET', 'POST'])
def seat(movie):
	rep = str(fl.request.data)
	return buySeat((movie,))
	
	#res = buySeat((movie,))
	#print(res)
	#return "OK"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=True)