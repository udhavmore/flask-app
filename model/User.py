import mysql.connector
import json

class User:
    def __init__(self):
        try:
            # Establising MySQL database connection
            self.con = mysql.connector.connect(host='localhost',username='root',password='root',database='flask-app')
            self.cur = self.con.cursor(dictionary=True) # Get the result in dictionary format
            print("Connection Successful!!!")
        except Exception as e:
            print(f"Error while connecting to database: {e}")

    def user_getall(self):
        """Get all the users from database"""
        self.cur.execute("SELECT * from user")
        result = self.cur.fetchall()
        if len(result) > 0:
            return json.dumps(result)
        else:
            return "No Data Found!!!"