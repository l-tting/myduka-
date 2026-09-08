from flask import Flask , render_template,request, redirect,url_for
from database import get_products, get_sales,get_stock,insert_products

# flask instance
app = Flask(__name__)

#home route
@app.route('/')   # decorator func
#view function
def home():
    name = "Alex"
    return render_template('index.html',name=name)

# http://127.0.0.1:5000/products
@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html',products=products)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST': 
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = ( product_name, buying_price, selling_price )
        insert_products(new_product)
        print("Product added successfully")
    return redirect(url_for('products'))



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