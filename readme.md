Open up a new terminal and run the following commands:
1.pip install flask
2.pip install psycopg2-binary

Open sql shell:
Once connected to postgres:
1.Create a new database called myduka
   create database myduka;
2.Next connect to that database
  \c myduka
3.Create tables using the following commands:


    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0),
        selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0)
    );

    CREATE TABLE stock (
        id SERIAL PRIMARY KEY,
        pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
        stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE sales (
        id SERIAL PRIMARY KEY,
        pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
        quantity INTEGER NOT NULL CHECK (quantity > 0),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        phone_number VARCHAR(100) NOT NULL,
        password VARCHAR(255) NOT NULL
    );

*Pre-requisites*:
*1.SQL* -> primary keys, foreign keys, relationships, sql queries , joins, aggeregate functions, sql clauses (where)
*2.Python* -> data types , data structures(lists and tuples),conditional statements, loops, functions



insert into stock(1,'eggs')

insert into products(name,buying_price,selling_price)values('milk',50,60);


*INTRODUCTION TO PSYCOPG2*
*PIP* -> Python package manager -> Pip Installs Packages -> used to download external libraries in Python 

*psycopg2* -> a database driver / adapter used to connect Python to a Postgres database
-> To establish this connection, we use the function *psycopg2.connect()*

*conn* - a variable representing our connection to the database
*psycopg2.connect()* - a function meant to create or establish a new database connection
-> To create this connection it needs some arguments:
*1.host*
=> on what server is your database hosted
=> localhost (your local device / pc)
*2.port*
=> where exactly in my pc / server do i find the Postgres service
=> 5432 : default Postgres port
*3.user*
 -> default Postgres username : postgres
*4.password*
-> password attached to a Postgres user
*5.dbname*
-> name of the database you want to connect to 




*domain name vs ip address*
*ip address* 
-> a number that is used to uniquely identify a device on a network
-> users trying to access an application must know the server's ip address beforehand
e.g*172.200.121.200*

*domain name* 
-> a human friendly name for an ip address that helps end users  access applications easily
-> e.g google server => *172.200.121.200* -> google.com

*dns* -> domain name system -> translates domain names into ip addresses

google.com  ---> dns lookup -> dns --> 172.200.121.200

your local device => has a default ip address of 127.0.0.1
127.0.0.1 -> ip address
localhost -> domain name for 127.0.0.1



*performing database operations with psycopg2*
-> to perform db operations , we use a cursor object 
*cur* -> object used to perform db operations
*cur.execute()* -> a function / method used by cursor object to execute sql queries
*cur.fetchall()* -> a function / method used to extract data from a Postgres environmnent and back to Python

[(136, 'milk', Decimal('50.00'), Decimal('60.00')), (137, 'bread', Decimal('55.00'), Decimal('65.00'))]

*N/B* -> expect your data from cur.fetchall() as a *list of tuples*
list -> entire dataset
tuple -> a single record / row in that dataset

*insert data with psycopg2*
cur.execute(insert query here...)
*conn.commit()* -> permanently saves your data in the db



*transaction states*
Active -> means an sql query is still running
Partially Committed -> query has finished running but the data has not been permanently saved in the database
Aborted  -> the query has been stopped before completion
Committed -> query finished running and data has been permanently saved in the database


insert data ----> partially committed ----> committed

*To have our insert functions be reusable we let it take parameter(s)*


*%s* -> represents psycopg2 placeholders 

*Task*
Using functions write 2 functions:
1.get_sales() 
2.insert_sales()


*sales per product*
select products.name , sum(sales.quantity * products.selling_price ) as total_sales from sales join products on 
sales.pid = products.id group by products.name;


*profit per day*
select date(sales.created_at) as day, sum((products.selling_price - products.buying_price) * sales.quantity) as total_profit from sales join products on sales.pid = products.id group by day;



*Multiline strings*
-> A string that spans more than a single line 
-> To use a multiline string we use triple opening and closing quotations

*Task*
Use psycopg2 to write functions that fetch the followng data :
*sales per day*
select date(sales.created_at) as day , sum(sales.quantity * products.selling_price) as t_sales from sales join products
on sales.pid = products.id group by day;
*profit per product*
select products.name as p_name , sum((products.selling_price - products.buying_price) * sales.quantity) as profit from
sales join products on sales.pid = products.id group by p_name;


*OBJECT ORIENTED PROGRAMMING*
-> OOP : The paradigm or concept of building programs around classes and objects

Primitive data types -> inbuilt data types 
int 
float
str
bool

Jane -> str

We have 2 broad classifications of data types:
1.Inbuilt data types -> come with the programming language e.g int, float, str, bool
2.User defined types -> custom types built using classes and objects to represent custom data 

 *class*
 -> A template for creating objects
 *object*
 ->An instance of a class

 blueprint used to build the house -> class
 the actual / real building -> object

Any class has 3 things:
*1.Identity*
    -> the unique name used to identify a class e.g. class Car
    -> Typically we give classes identities in title case
*2.State*
    -> represents data in a class
    -> answers the question: what does a class have?
    -> we use *attributes* to represent state
    ->*attributes* : are just variables inside a class
*3.Behaviour*
    -> represents what the class can do?
    -> this is enabled by use of *methods*
    -> *method*: is just a function inside a class


*examples*
class Car
1.Identity : Car
2.State -> no_of_wheels,engine_capacity,no_of_doors,is_electric,make
3.Behaviour -> start, stop, speed, park, carry_goods


class Student
class Dog

__init__() -> a constructor 
*constructor* -> a special method that is automatically called when creating an object ,used to 
   initialize an object with some values
   -> It has leading and trailing double underscores -> it is a *dunder method*
   -> *dunder* -> double underscore
   -> the purpose of the underscores is to identify this method as a special method
*self* -> refers to the object itself


*Task on OOP*
1.Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened 
2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info()
3.Create two BankAccount objects that can deposit, withdraw and display_info––



*N/B:-*
When passing default arguments in the __init__ constructor , it has to be the last argument passed


**INHERITANCE IN OOP**
-> A feature of OOP that allows one class to inherit or borrow features / properties from another class
*Parent class* 
 -> The class that is inherited from
 -> It is also called a base class or a super class
*Child class*
 -> the class that inherits from the parent
 -> It is also called a derived class or subclass

e.g. Animal -> Horse
     Person -> Student

Inheritance creates "Is -A" relationship
e.g Dog inherits from Animal ===>Dog is an Animal


*Types of Inheritance*
*1.Single level inheritance*
-> One child inherits from one parent
*2.Multiple inheritance*
-> One child inheriting from multiple parents
*3.Multilevel Inheritance*
-> One child class inherits from another child class
*4.Hierrarchical Inheritance*
-> Multiple child classes from one parent


*WHY INHERITANCE?* -> promotes reusability of programs and reduces redundancy

*super* -> this is a keyword that allows us to access the parent's methods from inside the child class

*method overriding*
-> when a child class provides its own implementation of a method that was already defined in the parent
class
-> the parent provides general behaviour while the child provides specific behaviour 

*Task on inheritance*

Python OOP — Inheritance Task: Vehicle Management System

Create a small vehicle management system using inheritance. Start by creating a parent class called Vehicle. The Vehicle class should have three attributes: brand, model, and year. It should have a display_info() method that prints the vehicle's basic information. Add a start() method that prints a simple message saying the vehicle has started, and a stop() method that prints a simple message saying the vehicle has stopped.

Next, create a child class called Car that inherits from Vehicle. A Car should have an additional attribute called number_of_doors. Add a simple drive() method that prints a message saying the car is driving. Override the display_info() method so that it also displays the number of doors. Inside the overridden method, use super() to call the parent's display_info() method.

Then create another child class called Motorcycle that also inherits from Vehicle. A Motorcycle should have an additional attribute called engine_cc, representing the engine size. Add a simple ride() method that prints a message saying the motorcycle is being ridden. Override display_info() so that it also displays the engine size. Again, use super() to call the parent's display_info() method.

Your class structure should look like this:

Vehicle
   ├── Car
   └── Motorcycle

The Vehicle class should have start(), stop(), and display_info() methods. The Car should have a drive() method, while the Motorcycle should have a ride() method. Both child classes should override display_info() and use super().

Finally, create one Car and one Motorcycle and test their methods

*Pillars of OOP*
*1.Inheritance*
*2.Polymorphism*
-> Method overloading : methods have same name but different signatures e.g different parameters
*3.Encapsulation*
-> bundling data and methods together
*4.Abstraction*
-> Hiding inner complex implementation and providing only what is necessary => uses abstract classes

*reference geeks for geeks for the above concepts*


*INTRODUCTION TO FLASK*
*framework vs library*

option1 -> framework
option2 -> library

*framework* - a collection of prebuilt code and tools that are meant to help developers build applications easily without having to start from scratch but they require the developer to follow strict rules that are set by the framework 

*examples of frameworks*
1.Python - Flask, FastAPI, Django
2.JavaScript - React, Vue, Angular, Svelte
3.Java - Spring
4.C# - .NET
5.PHP - Laravel
6.Golang - Chi, Gin
7.Ruby - Ruby on Rails
8.Rust - Tokio
9.C++ - Qt , Drogon

*flask* -> A python framework meant to build web applications

*Routing in Flask*
-> Routing is the mechanism of mapping / connecting URLs to Python functions . It is a system
for resource navigation
-> *URL* -> The full address that is used to access an application
example of a url=>*https://meet.google.com/dsh-idtb-oqb*
*parts of a url*
*1.Protocol*
 -> determines how data is transferred over a network 
 -> http or https 
 -> http : hypertext transfer protocol -> standard for sending data over a network for browsers
        -> sends data as raw text
 -> https : hypertext transfer protocol secure
        -> sends data in encrypted format
        -> end to end tls / ssl
*2.Domain*
-> human friendly name for an ip address e.g.www.google.com
*3.Path*
-> the specific resource to be accessed when using an application
-> e.g /users


=> Routing in flask is enabled through the use of a *decorator function* called *@app.route()*
*decorator function* -> a function that determines or modifies the behaviour of another function
 -> they have a signature '@' prefix

-> @app.route() can take some arguments:
    1.Path  -> e.g. /users , /, /products
    2.Method

@app.route('/') ----> decorator function
def home():       ---> view function
    return "Hello World!!"  ---> data to be returned


*index route* --> symbolized using / -> this is the route of the default landing page
*view function* -> the normal Python function meant to execute a specific task
*N/B* :- View functions cannot have shared names

https://techcamp.co.ke/
https://techcamp.co.ke/about-us
https://techcamp.co.ke/contact-us

https://techcamp.co.ke/
@app.route('/')
def home():
    return "Home page"



https://techcamp.co.ke/about-us
@app.route('/about-us')
def about_us():
    return "About Us page"


@app.route() -> / -> def home()
             -> /about-us -> def about_us()


-> instead of returning single pieces of data, we should instead return full html pages and then 
return as much data as we want in these pages
->To return html pages , we must have the following project structure:
>static
  -> all static files -> css , js , images , videos , icons , favicons
>templates
  -> all html pages /files
  -> a single html file is called a template


-> To display these html pages , we then use a function called *render_template()* which
is imported from flask


*task* 
-> create a well styled navbar having all routes in that nav and use href to pass the route value
-> the navbar should be consistent and appear across all html pages


**template inheritance**
-> a feature in Flask that allows us to build application pages from a parent page.
-> The parent page / template has all common features of the entire application
-> The child templates / pages then inherit from the parent
-> To do this, define all common features in the parent / base template then have the child templates inherit from the base
-> template inheritance is largely supported by a Flask feature called *Jinja*
-> block title : defines a block within which we are able to pass the title 
of any page that inherits from base
-> block content : allows a page that inherits from base to pass its own unique content 
==> Anything outside the block content appears across all inheriting pages
{% extends 'base.html' %} -> inherit from base.html 

*Task*
-> Recreate your navbar (use a Bootstrap navbar) and have it in base.html
-> ensure that navbar features across all inheriting pages
-> Do the same with a real footer 


**Jinja**
-> A templating engine integrated with Flask meant to render dynamic html pages
-> It is simply syntax that is used depending on whether we are trying to render simple data or use control structures 

-> jinja when rendering data : use {{ }}
-> jinja when using control structures : {% %} 
-> Jinja with control structures has to be initialized and terminated 

*Control Structures* -> building blocks of a programming language
-> Control structures in Python:
*1.Sequence* 
 -> A Python program executes top to bottom , left to right
*2.Selection*
-> Your program has decision making abilities ->  conditional statements
*3.Repitition* 
-> Your program can execute a task repeatedly -> iteration with loops

{% if .....%} ---> initialization


{% endif %} ---> termination


*Task on Jinja*
In the products route where we have the variable products = ['milk','eggs','shoes'] , use a for loop inside products.html to loop through the products and only display 'eggs' in a h1 tag


*Task*
-> Display the products data inside products.html using a Bootstrap table


[(1, 'milk', Decimal('50.00'), Decimal('60.00')), (2, 'bread', Decimal('50.00'), Decimal('60.00'))]


pid    name\

*Task*
1.Apply datatables for products and stock data
2.Style the home / landing page accordingly ->
    Header 
    CTA 
    Benefits of using the product
    Features 
    Trusted Logos
3.Style your navbar and footer accordingly
   Navbar -> space nav items  ->have register & login floated to the far right
          -> get a logo and unique name for your application
   Footer -> copyright & social media links 
   --> have consistent colours for both navbar and footer


*POSTING DATA IN FLASK*
-> Posting : sending a request from a client to a server
-> Http has a request -response structure
-> request : sending data from client to server
-> response : data / message from server to client

*POSTING PRODUCTS IN FLASK*
*workflow / process*
1.User is provided with a form to fill
2.The form should have all product related fields 
3.User will fill and submit this form to a route in the server
4.The server will extract data from the form using a request object
  N/B: data from the form is sent in key-value pair format
      -> the key is used to access the value
    -> the request object has access to some methods:
         1.request.method -> used to identify what method has been defined in the form
         2.request.form -> used to extract form data using its key
5.Data is then processed 
6.We reuse the insert_products() function after importing to add our new product
7.User is notified of successfull / failed request
8.User is redirected

   
*form checklist for posting data*
1.method attribute 
   -> method represents what a server can do with a resource / data
2.action attribute
   -> represents the route in which the data is to be submitted to
3.name attribute
   -> value of the name attribute represents the key that is used to access the data by the request object
4.input type
5.button of type submit


*http methods*
1.GET 
 -> move data from a server to a client
 -> e.g. displaying products / sales / stock
2.POST
  -> move data / resources from a client to a server as a request
  -> e.g.add products / login / register / send a tweet
3.PUT
  -> update an existing resource
  -> e.g.changing passwords / changing profile pics / changing prod name / prices
3.DELETE
  -> getting rid of a resource / data
  -> deleting products


p_name : "Eggs"
b_price : 17
s_price : 20


*redirection* -> taking a user from one resource to another 
-> to enable redirection, we use the function redirect(url_for(''))

redirect() -> redirect a user to another resource
url_for() -> thiis function takes the name of the view function in the route to be redirected to


*http status codes*
-> special codes / designated numbers meant to be a way for the server to respond to user requests or actions
-> they have categories based on the type of message

1.Informational responses
  -> General purpose responses
  -> the server has received a request and is contiuning to process it
  -> they start with 1xx
2.Successful responses
   -> Signify that a request was executed successfully
   -> start with 2xx
   -> e.g 200 -> OK 
      e.g 201 -> Created successfully => adding a product
3.Redirection responses
   -> represent redirection messages 
   -> start with 3XX
4.Client errors
   -> error on client side
   -> start with 4XX
5.Server errors
   -> error on server side
   -> start with 5XX 


   *task*
   -> Implement adding sales using a form in the sales page


   *posting with a form in a modal*

   select a product and quantity
           |
    we pick the product id of that product 
           |
    insert product id along with quantity

*Task*
1.modify add products form to use a modal 
2.implement posting stock with a modal



*flash notifications*
-> One time notifications to the user to give them feedback based on some action
-> Flash messages are enabled by flash() function which is imported from flask
-> flash() can take 2 arguments :
    1.Message -> the text to be displayed e.g. product added successfully
    2.Message category -> the type of message displayed
         
*Message Categories*
1.success : green
2.error/danger : red
3.warning : yellow
4.info : blue

N/B:- Flash messages are stored in a *session cookie*  ---> to secure them we use a secret key
*making purchases*
--> Goal: We want to make sales only from products that have enough stock
-> if a product has enough stock, complete sale otherwise if not, we fail to complete sale and notify user


100 eggs --> initial stock
sell 20
new stock value = 80


myduka_db=# select * from sales;
 id | pid | quantity |         created_at         
----+-----+----------+----------------------------
  1 |   1 |       20 | 2026-08-19 15:15:46.763464
  3 |   1 |       20 | 2026-08-19 15:16:18.429507
  4 |   2 |       10 | 2026-08-19 15:16:18.432971
  6 |   2 |       15 | 2026-08-19 15:49:05.265689
  7 |   2 |      120 | 2026-08-19 18:54:52.085746
  9 |   1 |       10 | 2026-09-09 15:17:29.260503
(6 rows)

myduka_db=# select * from stock;
 id | pid | stock_quantity |         created_at         
----+-----+----------------+----------------------------
  1 |   1 |            100 | 2026-08-19 15:31:27.92186
  2 |   2 |             50 | 2026-08-19 15:31:27.929297
  3 |   1 |            100 | 2026-08-19 16:09:05.873015
  4 |   2 |             50 | 2026-08-19 16:09:05.879158
  5 |   1 |            300 | 2026-08-19 18:58:49.423274
(5 rows)


sales => amount of product out
stock => product in

remaining stock = stock - sales per product

500 - 50 =

select sum(stock.stock_quantity) from stock where pid =


(10) => 10
(10,) => a tuple containing a single value of 10

*fetchone()*-> returns a tuple -> used when we return a single value 
*fetchall()*-> returns a list of tuples-> used when there is more than one value to be returned e.g products, sales , stock data

500 - 50 = 450

[(450,)] ---> [0][0]
(450,) ---> [0]

(500,) 
(50,)


adds a product ---> adds stock on that product ----> make sales on that product
 --> check stock again before making another sale

 adds a product ---> add no stock ----> make no sale
 add a product ---> add some stock ---> make no sale

 zero vs null / nil
 zero -> actual value --> 500 - 500 = 0
 null -> value doesnt exist to begin with 

 null - null --> error 
 200 - null --> error

 0 - 0 = 0
 200 - 0 = 200

 *AUTHENTICATION*
Authentication : process of verifying the identity of a user 
         -> use passwords, pins , biometrics
         -> asks the question 'who are you?'
Authorization
        -> determines the access rghts of a user in a system
        -> checks for what a user is allowed to do


  *User registration workflow*
1.User is provided with a registration form to fill
2.User fills all relevant credentials and submits the form
3.Form is submitted to register route in the server for processing
4.The request object extracts user information using the key(name attribute)
5.confirm that the user attempting to register hasnt already been registered using their email(unique)
6.If user exists,flash that user already exists and suggest they login instead
7.If user doesnt exist, hash their password and insert user into users table
8.Flash successful registration and redirect to login


1 - Jane Doe  - janedoe@gmail.com  -0712345678 - Jane@123


*Password Hashing*
-> Is the process of converting plain text data into an encrypted format that is hard to decipher / read / understand
-> Password hashing ensures passwords are protected by making them difficult to figure out

Jane@123----> $ey.99wnu99d93990djnju883hu992iiujhd99ejjdjd

N/B:- hashing a value always reproduces the same exact hash everytime

Jane@123----> $ey.99wnu99d93990djnju883hu992iiujhd99ejjdjd
Jane@123----> $ey.99wnu99d93990djnju883hu992iiujhd99ejjdjd
Jane@123----> $ey.99wnu99d93990djnju883hu992iiujhd99ejjdjd


person A ------> sending a file -----> hashed to produce a hash value ----> person B receives the file -> hash the
received file  ===> if the two hashes match it means the file has not tampered with


person A hashes the file -> 003mid09o3j99djd99dj
person B hashed the file -> 00wemnd662vvsjje9idj


*rainbow table attack* 
-> This is a type of attack launched by a hacker targetting common passwords and their hashed 

*password salting*
-> the process of adding random text to a plain text password before hashing it so that the end result becomes more complex

Abc@123kks9sjjsooso -> $ghye88djd00wkjkd00wkksoosposokduyy377dhhfooekkdkd


Google -> Abc@123 + e0oodejcdiid -> $e8ienj0mkw00-wkdkdkkfjkjfjjjfjf
Pinterest -> Abc@123 + 288uehhejm -> $fg299wmjkd002klke0pdkkdjudjjdjd

flask-bcrypt
pip install flask-bcrypt
  
print(5)

Computer works with only binaries (0 and 1)


hello world ------> bytes(0 and 1s)

ASCII

A -> 65 ----> 00101
a -> 97 ----> 10011


Unicode -> the universal representation of any character in any language in numeric format

$ -> U-449 --> unicode point ----> bytes
A -> U-1772
?

utf-8 ---> a way of converting unicode points to bytes and vice versa

print


hello ----> unicode point.  -----> bytes. -----> unicode -----> hello


Jane@123 + salt ----> hashing ----> bytes -----> decode with utf-8 ----> to get a string hash value like $2b$12$1CUX8fu4xGOHUdkRw7RQsORHnQkA6EQcG64x5gPd3qLjggzs75jje



*Login workflow*
1.User is provided with a form to fill
2.user fills in login credentials and submits the form
3.Form is submitted to login route for processing
4.request object extracts login data using request.form method
5.use the user's email to determine if they are registered
6.if user is not registered , notify to register instead and stop login
7.if user is registered , check if password is correct
8.if password is incorrect, notify with incorrect password message
9.if password is correct, store user session , redirect to dashboard and notify with success message 


janedoe@gmail.com
Jane@123

$2b$12$1CUX8fu4xGOHUdkRw7RQsORHnQkA6EQcG64x5gPd3qLjggzs75jje


*N/B:* ---> Hashing is a one way function , meaning once a plain text value is hashed to produce a hash value you cannot
decrypt the hash back to go back to the plain text

In that case, we take the user's password , salt and hash it with the same salt and then compare the 2 hashes 


*password hash*-> hashed password stored in the db
*candidate password* ---> password the user fills when attempting to log in 


*session*
http -> is stateless
     -> meaning that after a request is sent and a response given , the server doesnt recall any services given / accessed 


     user ----> sends request to server to get products page
     server ---> responds with the product page
    once the page is rendered / given , the server forgets everything

user logs in ---> access some page
when they try to access another page , they are told to login again

user logs in
server uses session remember a user
everytime a user sends a request, server checks if session is valid
if valid gives access, user doesnt have to login again


*cookie*
-> a small piece of data that a website asks your browser to store
*session*
-> a way for the server to remember who you are using specific info e.g email
*session cookie*
-> a cookie used to identify a user's session


session data we're storing ===> email
if email is not in session ---> user has not logged in


protect -> products page, sales page , stock page & dashboard page

-> there is no need to protect add products because add products occurs in the products -> same thing
for add sales and add stock