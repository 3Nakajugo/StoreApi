import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="Store", user="postgres", password="postgres", host="localhost", port="5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.connection.cursor().execute(
            "CREATE TABLE IF NOT EXISTS users(userid SERIAL PRIMARY KEY NOT NULL , username VARCHAR(20) NOT NULL, password VARCHAR(30) NOT NULL)")

        self.connection.cursor().execute(
            " CREATE TABLE IF NOT EXISTS sales(salesid SERIAL PRIMARY KEY NOT NULL,\
            date TIMESTAMPTZ DEFAULT NOW(), \
            item VARCHAR(100) NOT NULL, sale_quantity int NOT NULL,\
            total_price int NOT NULL )")

        self.connection.cursor().execute(
            " CREATE TABLE IF NOT EXISTS products(productid SERIAL PRIMARY KEY NOT NULL, \
            product_name VARCHAR(100) NOT NULL,quantity int NOT NULL, \
            unit_price int NOT NULL, category VARCHAR(20) NOT NULL,total_price int NOT NULL )")
