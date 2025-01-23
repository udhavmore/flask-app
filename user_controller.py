from app import app

@app.route('/user/signup')
def signup():
    return '<h1>User Signup Page</h1>'