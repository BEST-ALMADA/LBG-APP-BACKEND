from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/equipas', methods=['GET'])
def equipas():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/equipas/all', methods=['GET'])
def equipasAll():
    conn = mysqlConnection()
    query = "SELECT * FROM equipas;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/equipas/att', methods=['GET'])
def equipasAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM equipas;')
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

@app.route('/equipas/describe', methods=['GET'])
def equipasDescribe():
    if 'idEquipa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEquipa = request.args['idEquipa']
    conn = mysqlConnection()
    query = "SELECT * FROM equipas where idEquipa = '"+idEquipa+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/equipas/insert', methods=['GET'])
def equipasInsert():
    if 'idEquipa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEquipa = request.args['idEquipa']
    nome = request.args['nome']
    numMembros = request.args['numMembros']
    
    conn = mysqlConnection()
    query = "INSERT INTO equipas ( idEquipa, nome, numMembros ) VALUES( '"+idEquipa+"', '"+nome+"' , '"+numMembros+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/equipas/remove', methods=['GET'])
def equipasRemove():
    if 'idEquipa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEquipa = request.args['idEquipa']
    
    conn = mysqlConnection()
    query = "DELETE FROM equipas WHERE idEquipa='"+idEquipa+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/equipas/update', methods=['GET'])
def equipasUpdate():
    if 'idEquipa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    conn = mysqlConnection()
    idEquipa = request.args['idEquipa']
    
    if 'nome' not in request.args:
        query = "SELECT nome FROM equipas WHERE idEquipa='"+idEquipa+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']

    if 'numMembros' not in request.args:
        query = "SELECT numMembros FROM equipas WHERE idEquipa='"+idEquipa+"';"
        records = mysqlQuery(conn, query)
        numMembros = str(records[0][0])
    else:
        numMembros = request.args['numMembros']
    
    query = "UPDATE equipas SET nome='"+nome+"', numMembros='"+numMembros+"' WHERE idEquipa='"+idEquipa+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)