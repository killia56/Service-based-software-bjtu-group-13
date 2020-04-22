import sqlite3
conn = sqlite3.connect('user.db')
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
print(loginUser(('user1', 'password1',)))
createUser(('user1', 'password1',))
print(loginUser(('user1', 'password1',)))
print(searchUser(('user1',)))

conn.close()
