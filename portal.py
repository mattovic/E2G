from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://github.com/mattovic/E2G')

# get brands list
@app.route('/brands/', methods=['GET'])
def get_brands_list():
    return 'Brands list'

# get products list
@app.route('/brands/products/', methods=['GET'])
def get_products_list():
    return 'Products list'

# get product details or upload a product
@app.route('/brands/products/<product_id>', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        get_product_details()
    else:
        upload_product()

if __name__ == '__main__':
    app.debug = True
    app.run()
