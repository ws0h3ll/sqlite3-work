import sqlite3
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE login (id INTEGER PRIMARY KEY, uname TEXT NOT NULL, pword TEXT NOT NULL);''')
    conn.commit()
    conn.close()
def reg():
    uname = input("Please enter username : ")
    pword = input("Please enter a password : ")
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    params = (uname,pword)
    c.execute('INSERT INTO login VALUES (null,?,?)',params)
    conn.commit()
    conn.close()
def login():
    a=''
    uname = input('Enter your username : ')
    pword = input('Enter your password : ')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''SELECT pword FROM login WHERE uname = ?''',(uname,))
    real_pword = c.fetchall()
    conn.commit()
    conn.close()
    if pword == real_pword[0][0]:
        print('Welcome back ' + uname)
    else:
        print('Incorrect password')
if __name__ == "__main__":
    wtd = input('Create database (c), Register (r), login (l)')
    if wtd == "c":
        create_table()
    elif wtd == "r":
        reg()
    elif wtd == "l":
        login()
