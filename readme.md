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
*1.SQL* -> primary keys, foreign keys, relationships, sql queries , joins,    aggeregate functions, sql clauses (where)
*2.Python* -> data types , data structures(lists and tuples),conditional statements, loops, functions