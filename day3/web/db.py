import os
import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="flights",
        user="postgres",
        password="secret")
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'name text  NOT NULL,'
                                 'lastname text  NOT NULL)'
                                 )
cur.execute('INSERT INTO users (name, lastname)'
            'VALUES (%s, %s)',
            ('Pouria',
             'Jahandideh')
            )
cur.execute('INSERT INTO users (name, lastname)'
            'VALUES (%s, %s)',
            ('Sara',
             'Ahmadi')
            )

conn.commit()
cur.close()
conn.close()