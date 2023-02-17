from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/equipasEventos', methods=['GET'])
def equipasEventos():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/equipasEventos/all', methods=['GET'])
def equipasEventosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM equipasEventos;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/equipasEventos/att', methods=['GET'])
def equipasEventosAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM equipasEventos;')
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

@app.route('/equipasEventos/describe', methods=['GET'])
def equipasEventosDescribe():
    if 'idEquipaEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEquipaEvento = request.args['idEquipaEvento']
    conn = mysqlConnection()
    query = "SELECT * FROM equipasEventos where idEquipaEvento = '"+idEquipaEvento+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/equipasEventos/insert', methods=['GET'])
def equipasEventosInsert():
    if 'idEquipaEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEquipaEvento = request.args['idEquipaEvento']
    nome = request.args['nome']
    numMembros = request.args['numMembros']
    
    conn = mysqlConnection()
    query = "INSERT INTO equipasEventos ( idEquipaEvento, nome, numMembros ) VALUES( '"+idEquipaEvento+"', '"+nome+"' , '"+numMembros+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/equipasEventos/remove', methods=['GET'])
def equipasEventosRemove():
    if 'idEquipaEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEquipaEvento = request.args['idEquipaEvento']
    
    conn = mysqlConnection()
    query = "DELETE FROM equipasEventos WHERE idEquipaEvento='"+idEquipaEvento+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/equipasEventos/update', methods=['GET'])
def equipasEventosUpdate():
    if 'idEquipaEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    conn = mysqlConnection()
    idEquipaEvento = request.args['idEquipaEvento']
    
    if 'nome' not in request.args:
        query = "SELECT nome FROM equipasEventos WHERE idEquipaEvento='"+idEquipaEvento+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']

    if 'numMembros' not in request.args:
        query = "SELECT numMembros FROM equipasEventos WHERE idEquipaEvento='"+idEquipaEvento+"';"
        records = mysqlQuery(conn, query)
        numMembros = str(records[0][0])
    else:
        numMembros = request.args['numMembros']
    
    query = "UPDATE equipasEventos SET nome='"+nome+"', numMembros='"+numMembros+"' WHERE idEquipaEvento='"+idEquipaEvento+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)