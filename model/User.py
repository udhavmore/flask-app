import mysql.connector
import json

class User:
    def __init__(self):
        try:
            # Establising MySQL database connection
            self.con = mysql.connector.connect(host='localhost',username='root',password='root',database='flask-app')
            self.cur = self.con.cursor(dictionary=True) # Get the result in dictionary format
            self.con.autocommit = True  # Setting autocommit=True to automatically commit the changes into database
            print("Connection Successful!!!")
        except Exception as e:
            print(f"Error while connecting to database: {e}")

    def user_getall(self):
        """Get all the users from database"""
        self.cur.execute("SELECT * FROM user")
        result = self.cur.fetchall()
        if len(result) > 0:
            return json.dumps(result)
        else:
            return "No Data Found!!!"
    
    def user_add_one(self, data):
        """Add a users into the database"""
        query = f"INSERT INTO user(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')"
        print(query)
        self.cur.execute(query)
        return "User Created Successfully!!!"
    
    def user_update_one(self, data):
        """Update  entry for user in database"""
        query = f"UPDATE user SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']}"
        print(query)
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return "User updated Successfully!!!"
        else:
            return "Nothing to Update!!!"