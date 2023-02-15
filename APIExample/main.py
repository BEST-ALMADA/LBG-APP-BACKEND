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

@app.route('/att')
def att():
    conn = mysqlConnection()
    cursor = conn.cursor()
    query = "SHOW TABLES;"
    tables_unprocessed = mysqlQuery(conn, query)
    tables = [t[0] for t in tables_unprocessed]
    att = {}
    for table in tables:
        cursor.execute(f'SELECT * FROM {table};')
        column_names = [i[0] for i in cursor.description]
        data = cursor.fetchall()
        rows = []
        for row in data:
            row_dict = {}
            for i in range(len(column_names)):
                row_dict[column_names[i]] = row[i]
            rows.append(row_dict)
        att[table] = rows
    mysqlCloseConnection(conn)
    return jsonify(att)

app.run()