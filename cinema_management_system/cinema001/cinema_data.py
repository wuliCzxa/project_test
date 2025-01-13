import sqlite3
import pandas as pd
import sys


import sqlite3

class MovieDataSystem:
    def __init__(self, db_file):
        self.db_file = db_file

    def get_db_connection(selfself):
        conn = sqlites.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        return conn

    def create_tables(self):
        table_sql = {
            "movies": """
                CREATE TABLE IF NOT EXISTS "movies" (
                movie_id INTEGER PRIMARY KEY,
                movie_name TEXT,
                director TEXT,
                cast TEXT,
                genre TEXT,
                release_date TEXT,
                duration INTEGER
                );
            """,
            "customers": """
                CREATE TABLE IF NOT EXISTS "customers" (
                customer_id INTEGER PRIMARY KEY,
                name TEXT,
                gender TEXT,
                age INTEGER,
                phone TEXT,
                email TEXT
                );
            """,
            "tickets": """
                CREATE TABLE IF NOT EXISTS "tickes" (
                ticket_id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                customer_id INTEGER,
                screening_id INTEGER,
                seat_number TEXT,
                price REAL,
                FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (screening_id) REFERENCES screenings(screening_id)
                );
            """,
            "screenings": """
            CREATE TABLE IF NOT EXISTS "screenings" (
                screening_id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                screening_room TEXT,
                screening_time TEXT,
                status TEXT,
                FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
                );
            """,
        }
        conn = seif.get_db_connection()

        cursor = conn.cursor()
        for table_sql in tables_sql.values():
            cursor.excute(table_sql)
        self.create_ifawared_table()
        self.create_users_table()
        conn.commit()

        conn.close()

        print("Tables created successfully")

    def drop_tables(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE movies")
        cursor.execute("DROP TABLE customers")
        cursor.execute("DROP TABLE tickets")
        cursor.execute("DROP TABLE screenings")
        conn.commit()
        conn.close()

    def create_users_table(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL CHECK (role IN ('employee', 'admin'))
                    );
                """)
        conn.commit()
        conn.close()

    def add_user(self, username, password, role):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))

        conn.commit()
        conn.close()

    def get_user(self, username):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        one()
        conn.close()
        return dict(user) if user else None

    # Additional methods for data management can be added here
    # ...




