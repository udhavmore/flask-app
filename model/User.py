import mysql.connector
class User:
    def __init__(self):
        try:
            con = mysql.connector.connect(host='localhost',username='root',password='root',database='flask-app')
            print("Connection Successful!!!")
        except Exception as e:
            print(f"Error while connecting to database: {e}")
    def user_getall(self):
        # Connection establishment
        # Query execution code
        return "This is user_signup"