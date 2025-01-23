from app import app

@app.route('/product/add')
def product_add():
    return '<h1>Product Add page</h1>'