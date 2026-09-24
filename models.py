import sqlite3
from datetime import datetime, timedelta
from database import get_connection

class Member:
    
    def __init__(self, name, email, phone="", member_id=None):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        """save the new membre to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)", (self.name, self.email, self.phone)
        )
        conn.commit()
        self.member_id = cursor.lastrowid
        conn.close()
        return self.member_id

    @staticmethod
    def get_all():
        """ Retrieve all members from the database"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT member_id, name, email, phone FROM members")
        rows = cursor.fetchall()
        conn.close()
        return [
            Member(member_id=r[0], name=r[1], email=r[2], phone=r[3])
            for r in rows
        ]

class Equipment:
    def __init__(self, equipment_id=None, name=None, category=None, is_available=1):
        self.equipment_id = equipment_id
        self.name = name
        self.category = category
        self.is_available = is_available

    def save(self):
        """Save the new equipment to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO equipment (name, category, is_available) VALUES (?, ?, ?)",
            (self.name, self.category, self.is_available),
        )
        conn.commit()
        self.equipment_id = cursor.lastrowid
        conn.close()
        return self.equipment_id

    @staticmethod
    def get_available():
        """Retrieve all equipment from the database"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT equipment_id, name, categorie, is_available FROM equipment WHERE is_available = 1"
        )
        rows = cursor.fetchall()
        conn.close()
        return [
            Equipment(
                equipment_id=r[0], name=r[1], category=r[2], is_available=r[3]
                )
            for r in rows
        ]
class Loan:

    def __init__(self, loan_id=None, member_id=None, equipment_id=None, loan_date=None, return_date=None):

        self.loan_id = loan_id
        self.member_id = member_id
        self.equipment_id = equipment_id
        self.loan_date = loan_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.return_date = return_date

    def checkout(self):
        """create a loan record and update equipment availability to 0."""
        conn = get_connection()
        cursor = conn.cursor()

        #1.insert active loan record
        cursor.execute(
            """
            INSERT INTO loans (member_id, equipment_id, loan_date) VALUES (?, ?, ?)
            """,

                (self.member_id, self.equipment_id, self.loan_date),
            )
        self.loan_id = cursor.lastrowid

        #2.update equipment availability to 0
        cursor.execute(
            "UPDATE equipment SET is_available = 0 WHERE equipment_id = ?",
            (self.equipment_id,),
        )

        conn.commit()
        conn.close()
        return self.loan_id

    @staticmethod
    def return_item(loan_id):
        """Return equipment: record return date and set equipment as available (1)."""
        conn = get_connection()
        cursor = conn.cursor()

        # Check if active loan exists
        cursor.execute(
            "SELECT equipment_id FROM loans WHERE loan_id = ? AND return_date IS NULL",
            (loan_id,),
        )
        row = cursor.fetchone()

        if not row:
            conn.close()
            return False

        equipment_id = row[0]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Set return timestamp
        cursor.execute(
            "UPDATE loans SET return_date = ? WHERE loan_id = ?",
            (now, loan_id),
        )

        # Set equipment as available again (1)
        cursor.execute(
            "UPDATE equipment SET is_available = 1 WHERE equipment_id = ?",
            (equipment_id,),
        )

        conn.commit()
        conn.close()
        return True
