import mysql.connector
from datetime import date

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user = "root",
                password="Dheeraj@2004",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None