from app import app
from model.User import User

user = User()

@app.route('/user/getall')
def getallusers():
    return user.user_getall()