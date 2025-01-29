from app import app
from model.User import User
from flask import request

user = User()

@app.route('/user/getall')
def getallusers():
    return user.user_getall()

@app.route('/user/add', methods=['POST'])
def addoneuser():
    return user.user_add(request.form)

@app.route('/user/update', methods=['PUT'])
def updateuser():
    return user.user_update(request.form)

@app.route('/user/delete/<id>', methods=['DELETE'])
def deleteuser(id):
    return user.user_delete(id)

@app.route('/user/patch/<id>', methods=['PATCH'])
def patchuser(id):
    return user.user_patch(request.form, id)

@app.route('/user/getall/limit/<limit>/page/<page>')
def userpagination(limit, page):
    return user.user_pagination(limit, page)