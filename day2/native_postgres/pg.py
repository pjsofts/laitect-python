import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                  password="secret",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="flights")
                                  