import sqlite3
from datetime import datetime

conn = sqlite3.connect('user_queries.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    response_topic TEXT NOT NULL,
    user_query TEXT NOT NULL,
    ai_response TEXT NOT NULL,
    date TEXT NOT NULL,
    sos_status TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database and table created successfully.")