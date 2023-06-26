from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3

router = APIRouter()

class User(BaseModel):
    userId: str
    name: str
    email: str

@router.post("/users")
async def create_user(user: User):
    try:
        # Connect to the database (creates a new database if it doesn't exist)
        conn = sqlite3.connect('mydatabase.db')

        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        # Create a table
        cursor.execute("""
            INSERT INTO users (userId, name, email) 
            VALUES (?, ?, ?);
        """, (user.userId, user.name, user.email))
        conn.commit()

        return {"message": "User created successfully"}
    except sqlite3.Error as e:
        # Handle any potential database errors
        return {"error": str(e)}
    finally:
        # Close the database connection and cursor
        cursor.close()
        conn.close()

@router.get("/users/{userId}")
async def get_user_by_id(userId: str):
    try:
        # Connect to the database (creates a new database if it doesn't exist)
        conn = sqlite3.connect('mydatabase.db')

        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        # Execute the SQL query to retrieve the user by userId
        cursor.execute("SELECT * FROM users WHERE userId = ?", (userId,))

        # Fetch the result
        result = cursor.fetchone()

        # Check if a user was found
        if result:
            # Convert the result to a dictionary and return it
            columns = [column[0] for column in cursor.description]
            user_dict = dict(zip(columns, result))
            return user_dict
        else:
            # User not found, return an error message
            return {"error": "User not found"}
    except sqlite3.Error as e:
        # Handle any potential database errors
        return {"error": str(e)}
    finally:
        # Close the database connection and cursor
        cursor.close()
        conn.close()