from flask import Flask , render_template
from database import get_products, get_sales,get_stock


# flask instance
app = Flask(__name__)

#home route
@app.route('/')   # decorator func
#view function
def home():
    name = "Alex"
    return render_template('index.html',name=name)


@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html',products=products)


@app.route('/sales')
def sales():
    sales = get_sales()
    return render_template('sales.html',sales = sales)



@app.route('/stock')
def stock():
    stock = get_stock()
    return render_template('stock.html',stock = stock)



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')




app.run(debug=True)