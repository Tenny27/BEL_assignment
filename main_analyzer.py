# main_analyzer.py

import psycopg2
from psycopg2 import sql

class MainAnalyzer:
    def __init__(self, connection):
        self.connection = connection

    @staticmethod
    def create_connection():
        dbname = "postgres"
        user = "postgres"
        password = "1967"
        host = "localhost"
        port = "5432"

        connection = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )

        return connection

    def insert_record(self, user_id, timestamp, status):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    sql.SQL("""
                        INSERT INTO main_table(user_id, timestamp, final_status)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (user_id) DO UPDATE
                        SET timestamp = %s, final_status = %s
                    """),
                    (user_id, timestamp, status, timestamp, status)
                )
                self.connection.commit()
        except Exception as e:
            print(f"Error updating record: {e}")

    # Add other methods as needed
