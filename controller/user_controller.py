from app import app
from model.User import User

user = User()

@app.route('/user/signup')
def signup():
    return user.user_signup()