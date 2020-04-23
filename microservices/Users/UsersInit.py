import sqlite3
conn = sqlite3.connect('Users.db')
c = conn.cursor()


def createTabUser():
    c.execute('''CREATE TABLE users
             (login text, password text)''')
    conn.commit()

def createUser(t):
    c.execute("INSERT INTO users VALUES (?,?)", t)
    conn.commit()

def loginUser(t):
    c.execute('SELECT * FROM users WHERE login=? AND password=?', t)
    return c.fetchone()!=None

def searchUser(t):
    c.execute('SELECT * FROM users WHERE login=?', t)
    return c.fetchone()!=None


createTabUser()
createUser(('user1', 'password1',))
createUser(('user2', 'password2',))
createUser(('user3', 'password3',))

conn.close()
