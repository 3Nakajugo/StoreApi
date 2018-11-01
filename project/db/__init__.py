import psycopg2


conn = psycopg2.connect(host="localhost", database="test",
                        user="postgres", password="postgres")
