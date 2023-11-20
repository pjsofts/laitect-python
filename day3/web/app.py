import os
import psycopg2
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost", database="flights", user="postgres", password="secret"
    )
    return conn

@app.route("/users")
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, lastname FROM users;")
    users = cur.fetchall()

    result = []
    for user in users:
        result.append({"name": user[0], "lastname": user[1]})

    cur.close()
    conn.close()
    return result

@app.route("/users", methods = ["POST"])
def post_users():
    # validation
    data = request.get_json()
    name = data.get("name")
    lastname = data.get("lastname")

    if len(name) < 3 or len(lastname) < 3:
        return "name and last name should be longer than 3", 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_query = """ INSERT INTO users (name, lastname) VALUES (%s,%s)"""
        record = (name, lastname)
        cursor.execute(insert_query, record)
        conn.commit()
        return ""
    except Exception as e:
        print("some error happened", str(e))
        return  "internal sever error", 500
    
