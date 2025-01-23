from flask import Flask

app = Flask(__name__)

from controller.user_controller import signup
from controller.product_controller import product_add

@app.route('/')
def home():
    return '<h1>Ola Migo</h1>'


if __name__ == '__main__':
    app.run(debug=True)