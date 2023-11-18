import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="secret",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="flight")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO users (name, last) VALUES (%s,%s)"""
    record_to_insert = ('javad', 'javadi')
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into users table")
except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")