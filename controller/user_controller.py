from app import app
from model.User import User
from flask import request
from datetime import datetime

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

@app.route('/user/<id>/upload/avatar', methods=['PUT'])
def uploaduseravatar(id):
    file = request.files['avatar']
    time_now = str(datetime.now().timestamp()).replace(".", "")
    file_name_split = file.filename.split(".")
    file_ext = file_name_split[len(file_name_split)-1]
    unique_filename = time_now + "." + file_ext
    file_full_path = f"uploads/{unique_filename}"
    file.save(file_full_path)
    return user.user_upload_avatar(id, file_full_path)

@app.route('/uploads/<filename>')
def getuseravatar(filename):
    return user.user_avatar(filename)