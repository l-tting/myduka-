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

Pre-requisites:
*1.SQL* -> primary keys, foreign keys, relationships, sql queries , joins, aggeregate functions, sql clauses (where)
*2.Python* -> data types , data structures(lists and tuples),conditional statements, loops, functions



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



