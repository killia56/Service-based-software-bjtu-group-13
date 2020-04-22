import flask as fl
import sqlite3
import requests
conn = sqlite3.connect('Tiket.db')
c = conn.cursor()

app = fl.Flask(__name__)

def searchMovie(t):
	c.execute('SELECT * FROM movies WHERE movie=?', t)
	return c.fetchone()!=None
	conn.commit()

def createMovie(t):
	c.execute("INSERT INTO movies VALUES (?,?,?)", t)
	conn.commit()

def allMovies():
	return c.execute('SELECT * FROM movies')

def buySeat(t):
	c.execute('SELECT * FROM movies WHERE movie=?', t)
	tmp = c.fetchone()
	# print("seat bought for " + tmp[0] + " : " + str(tmp[2]) + "/" + str(tmp[1]) + " Success to bought : " + str(tmp[2] < tmp[1]))
	c.execute('UPDATE movies SET seatBought = seatBought + 1 WHERE movie=? AND seatBought < seat', t)
	conn.commit()
	return tmp[2] < tmp[1]

@app.route("/", methods=['GET'])
def index():
	return "T"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=True)