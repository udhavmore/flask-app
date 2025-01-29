import mysql.connector
import json
from flask import make_response

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
            res = make_response({"data": result}, 200)
            res.headers['Access-Control-Allow-Origin'] = '*'  # handling CORS for browsers
            return res
        else:
            return make_response({"message": "No Data Found!!!"}, 204)
    
    def user_add(self, data):
        """Add a users into the database"""
        query = f"INSERT INTO user(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')"
        print(query)
        self.cur.execute(query)
        return make_response({"message":"User Created Successfully!!!"}, 201)
    
    def user_update(self, data):
        """Update entry for user in database"""
        query = f"UPDATE user SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']}"
        print(query)
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return make_response({"message": "User updated Successfully!!!"}, 201)
        else:
            return make_response({"message": "Nothing to Update!!!"}, 202)
    
    def user_delete(self, id):
        """Delete user entry from database"""
        query = f"DELETE FROM user WHERE id={id}"
        print(query)
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return make_response({"message": "User deleted Successfully!!!"},200)
        else:
            return make_response({"message": "Nothing to Delete!!!"}, 202)
    
    def user_patch(self, data, id):
        """Update a field for user in database"""
        query = "UPDATE user SET "
        for key in data:
            query += f"{key}='{data[key]}',"
        query = query[:-1] + f" WHERE id={id}"
        print(query)
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return make_response({"message": "User updated Successfully!!!"}, 201)
        else:
            return make_response({"message": "Nothing to Update!!!"}, 202)
