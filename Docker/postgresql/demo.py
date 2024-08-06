import psycopg2
from psycopg2 import OperationalError

def create_database():
    try:
        # Connect to the default PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5433"
        )
        conn.autocommit = True

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the SQL command to create the database
        cursor.execute("CREATE DATABASE mydatabase;")

        print("Database created successfully!")

        # Close the cursor and connection to the default database
        cursor.close()
        conn.close()

    except OperationalError as e:
        print(f"Error: {e}")


# Create the database
create_database()

