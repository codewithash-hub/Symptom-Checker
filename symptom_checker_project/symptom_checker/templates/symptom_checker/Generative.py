import sqlite3
from datetime import datetime

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    user_query TEXT NOT NULL,
    ai_response TEXT,
    sos_status BOOLEAN NOT NULL DEFAULT 0
)
''')

# Create a table to store treatment plans
cursor.execute('''
CREATE TABLE IF NOT EXISTS treatment_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_query TEXT NOT NULL,
    ai_response TEXT NOT NULL,
    generated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
''')

def shorten_query(user_query, max_length=30):
    """
    Shortens the user's input query to a specified maximum length.
    
    Parameters:
    - user_query (str): The user's input query.
    - max_length (int): The maximum length for the short title. Default is 30 characters.
    
    Returns:
    - str: The shortened query.
    """
    if len(user_query) > max_length:
        return user_query[:max_length - 3] + '...'  # Truncate and add ellipsis
    else:
        return user_query  # Return the original query if it's within the limit

def generate_treatment_plan(user_query, ai_response):
    """
    Generates a treatment plan based on user query and AI response, and saves it to the database.
    
    Parameters:
    - user_query (str): The user's input query.
    - ai_response (str): The AI's response related to the query.
    """
    # Shorten the user query
    short_query = shorten_query(user_query)

    # Save the treatment plan to the database
    cursor.execute('''
    INSERT INTO treatment_plans (short_query, ai_response)
    VALUES (?, ?)
    ''', (short_query, ai_response))

    conn.commit()
    print("Treatment plan saved successfully.")

# fetch the populated data from the database(usersQuery)

user_input = "This is a very long user input query that needs to be shortened"
ai_response = "This is the AI's response to the user's query."

# Generate and save the treatment plan
generate_treatment_plan(user_input, ai_response)

# Close the connection
conn.close()