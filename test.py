import sqlite3
conn = sqlite3.connect('user.db')
c = conn.cursor()

def createTab():
    c.execute('''CREATE TABLE user
             (login text, password text)''')
    c.execute("INSERT INTO user VALUES ('user1','password1')")
    conn.commit()
#createTab()


def loginUser(t):
    c.execute('SELECT * FROM user WHERE login=? AND password=?', t)
    return c.fetchone()!=None

print(loginUser(('user1', 'password1')))
print(loginUser(('user2', 'password1')))

conn.close()
