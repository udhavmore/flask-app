import mysql.connector
import json
from flask import make_response, send_file

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
            res = make_response({"items": result}, 200)
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
    
    def user_pagination(self, limit, page):
        """Get user records page-by-page"""
        limit, page = int(limit), int(page)
        start = (page*limit) - limit
        query = f"SELECT * FROM user LIMIT {start}, {limit}"
        self.cur.execute(query)
        result = self.cur.fetchall()
        if len(result) > 0:
            res = make_response({"items": result, "page": page, "limit": limit}, 200)
            res.headers['Access-Control-Allow-Origin'] = '*'  # handling CORS for browsers
            return res
        else:
            return make_response({"message": "No Data Found!!!"}, 204)
    
    def user_upload_avatar(self, id, file_path):
        """Upload avatar for user and store the URL for avatar into the database"""
        query = f"UPDATE user SET avatar='{file_path}' WHERE id={id}"
        print(query)
        self.cur.execute(query)
        if self.cur.rowcount>0:
            return make_response({"message": "File uploaded successfully!!!"}, 201)
        else:
            return make_response({"message": "Nothing to Update!!!"}, 202)
    
    def user_avatar(self, filename):
        """Show user avatar"""
        return send_file(f"uploads/{filename}")