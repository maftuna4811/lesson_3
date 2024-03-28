import psycopg2 as db
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("DB_DATABASE"),
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"))

        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "update", "delete", "create"]

        if query_type in data:
            database.commit()

            if query_type == "insert":
                return "Inserted Data"

            elif query_type == "update":
                return "Updated Data"

            elif query_type == "create":
                return "Created Data"

            elif query_type == "drop":
                return "Drop Data"

        else:
            return cursor.fetchall()