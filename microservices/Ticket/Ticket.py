import flask as fl
import sqlite3
import requests
from flask import jsonify

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
	return {'message' : 'welcome in Ticket microservice'}, 200

@app.route("/TicketList", methods=['GET'])
def return_list():
	ticketlist = []
	for row in allMovies():
		ticketlist.append(row)
	print(ticketlist)
	return jsonify(ticketlist), 200

@app.route('/createMovie', methods=['GET', 'POST'])
def movieCreation():
	if fl.request.method == 'POST':
		if not fl.request.form:
			return {'message' : 'body is empty'}, 400
		else:
			movieName = str(fl.request.form['movieName'])
			seatnb = str(fl.request.form['seatnb'])
			soldnb = str(fl.request.form['soldnb'])
			if (not movieName and seatnb and soldnb):
				return {'message' : 'body require movieName, seatnb and soldnb'}, 400
			if searchMovie((movieName,)) == False:
				createMovie((movieName, seatnb, soldnb))
				return {'message' : 'movie created'}, 200
	else:
		return {'message' : 'login require POST data'}, 405

@app.route('/buySeat', methods=['GET', 'POST'])
def seat():
	if fl.request.method == 'POST':
		if not fl.request.form:
			return {'message' : 'body is empty'}, 400
		else:
			movie = str(fl.request.form['movie'])
			if not movie:
				return {'message' : 'body require movie'}, 400
			if buySeat((movie,)) == True:
				return {'message' : 'Seat is sold'}, 200
			else :
				return {'message' : 'Error with solding ticket'}, 400
	else:
		return {'message' : 'login require POST data'}, 405


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=True)