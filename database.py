import psycopg2

# establishing a new db connection
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='6979',dbname='myduka_db')


#creating a cursor object to perform db operations
cur = conn.cursor()


def get_products():
    cur.execute('select * from products')
    products = cur.fetchall()
    return products



def insert_products(product_values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",product_values)
    conn.commit()

product1 = ('hp probook',35000,40000)
product2 = ('shoes',1000,2000)

# insert_products(product1)
# insert_products(product2)


# products = get_products()
# print(products)


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales



def insert_sales(sale_values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",sale_values)
    conn.commit()

# sale1 = (2,20)
# sale2 = (1,10)
# insert_sales(sale1)
# insert_sales(sale2)

# sales = get_sales()
# print(sales)


def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

def insert_stock(stock_values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",stock_values)
    conn.commit()


# stock1 = (1,100)
# stock2 = (2,50)
# insert_stock(stock1)
# insert_stock(stock2)

# stock_data = get_stock()
# print(stock_data)



def get_sales_per_product():
    cur.execute("""
            select products.name , sum(sales.quantity * products.selling_price ) as total_sales 
            from sales join products on  sales.pid = products.id group by products.name;
     """)
    sales_per_product = cur.fetchall()
    return sales_per_product

# sales_per_product = get_sales_per_product()
# print(sales_per_product)



def get_profit_per_day():
    cur.execute("""
        select date(sales.created_at) as day, sum((products.selling_price - products.buying_price) * sales.quantity) as 
        total_profit from sales join products on sales.pid = products.id group by day;
    """)
    profit_per_day = cur.fetchall()
    return profit_per_day


profit_per_day = get_profit_per_day()
print(profit_per_day)


def get_sales_per_day():
    cur.execute("""
        select date(sales.created_at) as day , sum(sales.quantity * products.selling_price) as t_sales from sales join products
        on sales.pid = products.id group by day;
    """)
    sales_per_day = cur.fetchall()
    return sales_per_day


def get_profit_per_product():
    cur.execute("""
        select products.name as p_name , sum((products.selling_price - products.buying_price) * sales.quantity) as profit from
        sales join products on sales.pid = products.id group by p_name;
    """)
    profit_per_product = cur.fetchall()
    return profit_per_product

