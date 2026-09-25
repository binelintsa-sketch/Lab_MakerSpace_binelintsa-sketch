import sqlite3

DB_NAME = "makerspace.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Members table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT
            )
        """)
        
        # Equipment table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipment (
                equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT,
                is_available INTEGER DEFAULT 1
            )
        """)
        
        # Loans table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER,
                equipment_id INTEGER,
                loan_date TEXT,
                return_date TEXT,
                FOREIGN KEY(member_id) REFERENCES members(member_id),
                FOREIGN KEY(equipment_id) REFERENCES equipment(equipment_id)
            )
        """)
        conn.commit()