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

insert_products(product1)
insert_products(product2)


products = get_products()
print(products)



  