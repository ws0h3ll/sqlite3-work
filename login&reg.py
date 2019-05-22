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
    attempt = True
    while attempt == True:
        uname = input('Enter your username : ')
        pword = input('Enter your password : ')
        if uname == '' or pword == '':
            print('you failed to enter text into one of the text boxes...... exitting')
            break
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''SELECT pword FROM login WHERE uname = ?''',(uname,))
        real_pword = c.fetchall()
        conn.commit()
        conn.close()
        try:
            if pword == real_pword[0][0]:
                print('Welcome back ' + uname)
                attempt = False
            else:
                print('Incorrect password')
                again = input('Would you like to retry? (y)/(n)')
                if again == 'y':
                    pass
                else:
                    attempt = False
        except IndexError:
            print('user not found')
            break
if __name__ == "__main__":
    wtd = input('Create database (c), Register (r), login (l)')
    if wtd == "c":
        create_table()
    elif wtd == "r":
        reg()
    elif wtd == "l":
        login()
