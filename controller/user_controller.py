from app import app
from model.User import User
from flask import request

user = User()

@app.route('/user/getall')
def getallusers():
    return user.user_getall()

@app.route('/user/addone', methods=['POST'])
def addoneuser():
    return user.user_add_one(request.form)

@app.route('/user/updateone', methods=['PUT'])
def updateuser():
    return user.user_update_one(request.form)