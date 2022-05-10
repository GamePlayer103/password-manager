import sys
import sqlite3

DB_PATH = './passwords.db'      # path to database file

def input_args(args):
    """
    Get input from user and handle KeyboardInterrupt
    
    args -- a tuple of arguments to get from user
    """
    data = []
    print('Press [enter] to skip, ctrl-c to cancel\n')
    for arg in args:
        try:
            input_data = input(arg + ': ')
        except KeyboardInterrupt:
            print('\npressed ctrl-c, aborting')
            sys.exit()
        data.append(input_data)
    return data

def print_help():
    """
    Print help message
    """
    msg = (
        'usage:\n'
        '\tnew - add new password\n'
        '\tlist - print passwords\n'
        '\tedit - edit password\n',
        '\tdelete - delete password'
    )
    print(msg)

def create_connection(db_file):
    """
    Create connection with database

    db_file -- path to database file
    returns: connection object or None if failed
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def init_tables():
    """
    Setup password table in database if it not exist
    """
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
    """
    Add new password to database
    """
    args = input_args(('name', 'email', 'username', 'password', 'notes'))
    sql = ''' INSERT INTO passwords(name, email, username, password, notes)
            VALUES(?,?,?,?,?)'''
        
    conn = create_connection(DB_PATH)
    c = conn.cursor()
    c.execute(sql, args)
    conn.commit()

def print_passwords():
    """
    Print a list of all passwords from database
    """
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

def edit_password():
    """
    Edit password in database by it's id
    """
    args = input_args(('id', 'new password'))
    order = [1, 0]
    args = [args[i] for i in order]

    sql = ''' UPDATE passwords
            SET password = ?
            WHERE id = ? '''

    conn = create_connection(DB_PATH)
    c = conn.cursor()
    c.execute(sql, args)
    conn.commit()

def delete_password():
    """
    Delete password from database by it's id
    """
    args = input_args(('id',))

    sql = 'DELETE FROM passwords WHERE id = ?'

    conn = create_connection(DB_PATH)
    c = conn.cursor()
    c.execute(sql, args)
    conn.commit()

if __name__ == '__main__':
    init_tables()

    # Print help message if there is not arguments
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
        edit_password()
    elif arg == 'delete':
        delete_password()
    else:
        print_help()