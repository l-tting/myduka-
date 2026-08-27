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
