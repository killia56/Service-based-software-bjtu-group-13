import sqlite3
conn = sqlite3.connect('Payment.db')
c = conn.cursor()


def createTabTicket():
    c.execute('''CREATE TABLE tickets
             (user text, movie text, paid int)''')
    conn.commit()

def createTicket(t):
    c.execute("INSERT INTO tickets VALUES (?,?,0)", t)
    conn.commit()

def ticketPaid(t):
    c.execute('SELECT * FROM tickets WHERE user = ? AND movie=?', t)
    tmp = c.fetchone()
    c.execute('UPDATE tickets SET paid = 1 WHERE user=? AND movie = ?', t)
    conn.commit()
    return tmp[2]==0

def searchTicket(t):
    c.execute('SELECT * FROM tickets WHERE user = ? AND movie=?', t)
    return c.fetchone()!=None

def allTickets():
    return c.execute('SELECT * FROM tickets')


createTabTicket()
createTicket(('user1', 'movie1',))
createTicket(('user1', 'movie2',))
createTicket(('user1', 'movie3',))

conn.close()
