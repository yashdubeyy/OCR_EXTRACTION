import psycopg2
import json

# Database connection details (change as per your setup)
DB_NAME = "mydb"
DB_USER = "postgres"
DB_PASSWORD = "narnia"
DB_HOST = "localhost"
DB_PORT = "5432"

# Function to insert extracted JSON data into the database
def insert_data_to_db(data):
    import psycopg2

    conn = psycopg2.connect(
        dbname="add_your_database_name_her",
        user="add_your_username_here",
        password="add_your_password_here",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Replace "Unknown" with None (NULL in SQL)
    patient_name = None if data["patient_name"] == "Unknown" else data["patient_name"]
    dob = None if data["dob"] == "Unknown" else data["dob"]

    cur.execute("INSERT INTO patients (name, dob) VALUES (%s, %s) RETURNING id", (patient_name, dob))

    conn.commit()
    cur.close()
    conn.close()
