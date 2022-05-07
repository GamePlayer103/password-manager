import sys
import sqlite3

DB_PATH = './passwords.db'

def print_help():
    msg = (
        'usage:\n'
        '\tnew - add new password\n'
        '\tlist - print saved passwords\n'
        '\tedit - edit saved password\n'
    )
    print(msg)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def init_tables():
    sql = """ CREATE TABLE IF NOT EXISTS passwords (
                id integer PRIMARY KEY, 
                name text,
                email text,
                username text,
                password text,
                notes text
            ); """
    
    conn = create_connection(DB_PATH)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)
    else:
        print('error! cannot create database connection')

def add_password():
    try: 
        name = input('name: ')
        email = input('email: ')
        username = input('username: ')
        password = input('password: ')
        notes = input('notes: ')
    except KeyboardInterrupt:
        print('\npressed ctrl-c, aborting')

    data = (name, email, username, password, notes)
    sql = ''' INSERT INTO passwords(name, email, username, password, notes)
            VALUES(?,?,?,?,?)'''
        
    conn = create_connection(DB_PATH)
    c = conn.cursor()
    c.execute(sql, data)
    conn.commit()

def print_passwords():
    conn = create_connection(DB_PATH)
    c = conn.cursor()
    
    sql = 'SELECT * FROM passwords'
    c.execute(sql)

    rows = c.fetchall()

    print('ID | NAME | E-MAIL | USERNAME | PASSWORD | NOTES', end='\n\n')
    
    for row in rows:
        for col in row:
            print(f'{col}, ', end='')
        print('')

if __name__ == '__main__':
    init_tables()

    try:
        arg = sys.argv[1].lower()
    except IndexError:
        print_help()
        sys.exit()

    if arg == 'new':
        add_password()
    elif arg == 'list':
        print_passwords()
    elif arg == 'edit':
        pass
    else:
        print_help()