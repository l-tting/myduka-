from flask import Flask 

# flask instance
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!!"


@app.route('/products')
def products():
    return "My products"


@app.route('/sales')
def sales():
    return "Sales"


@app.route('/stock')
def stock():
    return "My stock"


@app.route('/dashboard')
def dashboard():
    return "Dashboard"



app.run()