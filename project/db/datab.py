import os
import psycopg2


class Database:

    def __init__(self):
        try:
            if os.getenv('APP_SETTINGS') == 'testing':
                database = 'testdb'
            else:
                database = 'Store'
            ''' create connection'''
            self.connection = psycopg2.connect(
                dbname=database, user="postgres", password="postgres", host="localhost", port="5432")
            self.cursor = self.connection.cursor()
            self.connection.autocommit = True
        except:
            print("cannot connect succesfully")

    def create_table(self):
        ''' create table users '''
        self.connection.cursor().execute(
            "CREATE TABLE IF NOT EXISTS users(userid SERIAL PRIMARY KEY NOT NULL , \
            username VARCHAR(20) NOT NULL, password VARCHAR(30) NOT NULL, role VARCHAR(30) NOT NULL)")

        '''create table sales'''
        self.connection.cursor().execute(
            " CREATE TABLE IF NOT EXISTS sales(salesid SERIAL PRIMARY KEY NOT NULL,\
            date TIMESTAMPTZ DEFAULT NOW(), \
            item VARCHAR(100) NOT NULL, sale_quantity int NOT NULL,\
            total_price int NOT NULL )")

        ''' create table products'''
        self.connection.cursor().execute(
            " CREATE TABLE IF NOT EXISTS products(productid SERIAL PRIMARY KEY NOT NULL, \
            product_name VARCHAR(100) NOT NULL,quantity int NOT NULL, \
            unit_price int NOT NULL, category VARCHAR(20) NOT NULL )")

    '''method for creating rowa in products table'''

    def post_products(self, product_name, quantity, unit_price, category):

        create = (
            """INSERT INTO products(product_name,quantity,unit_price,category) VALUES ('{}','{}','{}','{}')""".format(product_name, quantity, unit_price, category))

        self.connection.cursor().execute(create)

    '''method for getting all items from products table'''

    def get_products(self):
        command = """ SELECT * FROM products """

        self.cursor.execute(command)
        all_products = self.cursor.fetchall()
        return all_products

    ''' method to get single product '''

    def get_single_product(self, productid):

        command = (
            """ SELECT * FROM products WHERE productid='{}' """.format(productid))
        self.cursor.execute(command)
        single_prod = self.cursor.fetchone()
        return single_prod

    '''method to delete product'''

    def delete_product(self, productid):
        query = (""" DELETE FROM products WHERE productid='{}'""".format(productid))
        self.cursor.execute(query)

    '''method checks if product already exists'''

    def check_product(self, product_name):
        check = (
            """ SELECT * FROM products WHERE product_name ='{}'""".format(product_name))
        self.cursor.execute(check)

    ''' method to update a product'''

    # def update_product(self, productid):
    #     query = (""" UPDATE FROM product """)

    def post_user(self, username, password, role):
        create_user = (
            """INSERT INTO users(username ,password, role) VALUES ('{}','{}','{}')""".format(username, password, role))

        self.cursor.execute(create_user)

    def login(self, username, password):
        user_login = (
            """ SELECT * FROM users WHERE username= '{}' AND password ='{}' """. format(username, password))
        self.cursor.execute(user_login)
        user = self.cursor.fetchone()
        return user
