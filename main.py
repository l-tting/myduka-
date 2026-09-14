from flask import Flask , render_template,request, redirect,url_for,flash
from database import get_products, get_sales,get_stock,insert_products,insert_sales,insert_stock,available_stock

# flask instance
app = Flask(__name__)

app.secret_key = '99enjju993jdi909ewjkkjd00wjs93293'

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
        flash("Product added successfully",'success')
        
    return redirect(url_for('products'))



@app.route('/sales')
def sales():
    sales = get_sales()
    products = get_products()
    return render_template('sales.html',sales = sales,products = products)


@app.route('/make_sale',methods=['GET','POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid, quantity)
        
        check_stock = available_stock(pid)
        if check_stock < float(quantity):
              flash(f"Insufficient stock to complete sale, only {check_stock} available ",'danger')
              return redirect(url_for('sales'))
        
        insert_sales(new_sale)
        flash("Sale made successdfully",'success')

    return redirect(url_for('sales'))


@app.route('/stock')
def stock():
    stock = get_stock()
    products = get_products()
    return render_template('stock.html',stock = stock,products = products)


@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        pid = request.form['pid']
        stock_quantity = request.form['s_quantity']

        new_stock= (pid, stock_quantity)
        insert_stock(new_stock)

        flash("Stock added successdfully",'success')

    return redirect(url_for('stock'))



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