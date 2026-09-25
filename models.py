import sqlite3
from database import get_connection

class Member:
    def __init__(self, name, email, phone="",  member_id=None):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)",
                (self.name, self.email, self.phone)
            )
            conn.commit()
            self.member_id = cursor.lastrowid
            return self.member_id

    @classmethod
    def get_all(cls):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT member_id, name, email, phone FROM members")
            rows = cursor.fetchall()
            return [cls(name=row[1], email=row[2], phone=row[3], member_id=row[0]) for row in rows]

    @classmethod
    def search(cls, term):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT member_id, name, email, phone FROM members WHERE member_id = ? OR name LIKE ?",
                (term, f"%{term}%")
            )
            rows = cursor.fetchall()
            return [cls(name=row[1], email=row[2], phone=row[3], member_id=row[0]) for row in rows]

    @classmethod
    def delete(cls, member_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM loans WHERE member_id = ?", (member_id,))
            cursor.execute("DELETE FROM members WHERE member_id = ?", (member_id,))
            conn.commit()
            return cursor.rowcount > 0


class Equipment:
    def __init__(self, title, category="", is_available=1, equipment_id=None):
        self.equipment_id = equipment_id
        self.title = title
        self.category = category
        self.is_available = is_available

    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO equipment (title, category, is_available) VALUES (?, ?, ?)",
                (self.title, self.category, self.is_available)
            )
            conn.commit()
            self.equipment_id = cursor.lastrowid
            return self.equipment_id

    @classmethod
    def get_available(cls):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT equipment_id, title, category, is_available FROM equipment WHERE is_available = 1"
            )
            rows = cursor.fetchall()
            return [cls(title=row[1], category=row[2], is_available=row[3], equipment_id=row[0]) for row in rows]


class Loan:
    def __init__(self, member_id, equipment_id, loan_date=None, return_date=None, loan_id=None):
        self.loan_id = loan_id
        self.member_id = member_id
        self.equipment_id = equipment_id
        self.loan_date = loan_date
        self.return_date = return_date

    @classmethod
    def get_returned_loans(cls):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT m.member_id, m.name, e.title, l.loan_date, l.return_date
                FROM loans l
                JOIN members m ON l.member_id = m.member_id
                JOIN equipment e ON l.equipment_id = e.equipment_id
                WHERE l.return_date IS NOT NULL
                ORDER BY l.return_date DESC
                """
            )
            return cursor.fetchall()