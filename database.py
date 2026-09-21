import sqlite3
DB_NAME = 'makerspace.db'

def get_connection():
    """create and return a connection to the sqlite database"""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_tables():
    """create the tables in the database if they do not already exist"""
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Members table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT
        );
    '''
                   )

    # 2. Equipment Table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS equipment (
            equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            categorie TEXT NOT NULL,
            is_available INTEGER NOT NULL DEFAULT 1 CHECK (is_available IN (0, 1))
        );
    '''
    )

    # Create tools table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            available BOOLEAN NOT NULL DEFAULT 1
        );
    ''')

    # 3. Loans table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS loans (
            loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            equipment_id INTEGER NOT NULL,
            loan_date TEXT NOT NULL,
            return_date TEXT,
            FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
            FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
        );
    '''
    )

    conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()