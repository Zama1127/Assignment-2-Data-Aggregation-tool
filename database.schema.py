import sqlite3

# Define the schema for the SQLite database
schema_sql = """
CREATE TABLE IF NOT EXISTS csv_data (
    id INTEGER PRIMARY KEY,
    column1 number,
    column2 Province,
    column3 INTEGER
);

CREATE TABLE IF NOT EXISTS html_data (
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT
);
"""

def create_database():
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('data_aggregation.db')
        cursor = conn.cursor()

        # Execute the SQL statements to create tables
        cursor.executescript(schema_sql)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print("Database and tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating database:", e)

# Call the function to create the database
create_database()
