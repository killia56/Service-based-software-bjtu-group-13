import sqlite3
conn = sqlite3.connect('movie.db')
c = conn.cursor()


def createTabMovies():
    c.execute('''CREATE TABLE movies
             (movie text, seat int, seatBought int)''')
    conn.commit()

def createMovie(t):
    c.execute("INSERT INTO movies VALUES (?,?,?)", t)
    conn.commit()

def searchMovie(t):
    c.execute('SELECT * FROM movies WHERE movie=?', t)
    return c.fetchone()!=None

def allMovies():
    return c.execute('SELECT * FROM movies')

def buySeat(t):
    c.execute('SELECT * FROM movies WHERE movie=?', t)
    tmp = c.fetchone()
    # print("seat bought for " + tmp[0] + " : " + str(tmp[2]) + "/" + str(tmp[1]) + " Success to bought : " + str(tmp[2] < tmp[1]))
    c.execute('UPDATE movies SET seatBought = seatBought + 1 WHERE movie=? AND seatBought < seat', t)
    conn.commit()
    return tmp[2] < tmp[1]


createTabMovies()
print(searchMovie(('movie1',)))
createMovie(('movie1', 100, 0,))
createMovie(('movie2', 50, 0,))
print(buySeat(('movie1',)))
print(searchMovie(('movie1',)))
for row in allMovies():
    print(row)

conn.close()
