import psycopg2


conn = psycopg2.connect(host="localhost", database="Store",
                        user="postgres", password="postgres")
