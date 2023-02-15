from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery
from configApp import app
import pessoas
import equipas
import empresas

@app.route('/', methods=['GET'])
def home():
    conn = mysqlConnection()
    query = "SHOW TABLES;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/all', methods=['GET'])
def all():
    conn = mysqlConnection()
    query = "SHOW TABLES;"
    records = mysqlQuery(conn, query)

    data = {}
    for record in records:
        table_name = record[0]
        query = f"SELECT * FROM {table_name};"
        data[table_name] = mysqlQuery(conn, query)

    mysqlCloseConnection(conn)
    return jsonify(data)

app.run()

