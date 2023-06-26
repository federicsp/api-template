import sqlite3

def initialize_database():
    # Connect to the database (creates a new database if it doesn't exist)
    with sqlite3.connect('mydatabase.db') as conn:
        # Create a cursor object to execute SQL statements
        with conn.cursor() as cursor:
            # Create table users
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    userId INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')

        # Commit the changes (automatically done when exiting the context)
        conn.commit()

# Create table users
initialize_database()