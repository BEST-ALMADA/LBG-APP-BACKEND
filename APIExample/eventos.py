from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/eventos', methods=['GET'])
def eventos():
    accessPoints = ["all", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/eventos/all', methods=['GET'])
def eventosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM eventos;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/eventos/att', methods=['GET'])
def eventosAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM eventos;')
    column_names = [i[0] for i in cursor.description]
    data = cursor.fetchall()
    rows = []
    for row in data:
        row_dict = {}
        for i in range(len(column_names)):
            row_dict[column_names[i]] = row[i]
        rows.append(row_dict)
    mysqlCloseConnection(conn)
    return jsonify(rows)

#TODO