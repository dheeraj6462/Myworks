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

class GymMemberManager(DbConnect):

    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from members where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

connection_instance=DbConnect()
connection_instance.get_connection()