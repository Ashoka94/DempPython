import mysql.connector
from mysql.connector import Error
import os

# Parse the DB connection string and SSL configuration (Assuming the connection string contains required info)
db_config = {
    'user': 'root',
    'password': 'Password',
    'host': 'localhost',
    'database': 'pythodb',
    'port': 3306
}


# Function to load jobs from the database
def load_jobs_from_db():
    connection = None  # Initialize connection as None
    cursor = None  # Initialize cursor as None
    try:
        connection = mysql.connector.connect(**db_config)
        print("connection.is_connected()", connection.is_connected())
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM jobs")
            jobs = cursor.fetchall()  # Fetch all rows as dictionaries
            return jobs
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Function to load a single job by ID
# def load_job_from_db(job_id):
#     try:
#         connection = mysql.connector.connect(**db_config)
#         if connection.is_connected():
#             cursor = connection.cursor(dictionary=True)
#             cursor.execute("SELECT * FROM jobs WHERE id = %s", (job_id, ))
#             rows = cursor.fetchall()
#             if len(rows) == 0:
#                 return None
#             return rows[0]
#     except Error as e:
#         print(f"Error: {e}")
#         return None
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# # Function to add an application to the database
# def add_application_to_db(job_id, data):

#     try:
#         connection = mysql.connector.connect(**db_config)
#         if connection.is_connected():
#             cursor = connection.cursor()
#             query = """
#                 INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#             """
#             cursor.execute(query,
#                            (job_id, data['full_name'], data['email'],
#                             data['linkedin_url'], data['education'],
#                             data['work_experience'], data['resume_url']))
#             connection.commit()  # Commit the transaction
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
