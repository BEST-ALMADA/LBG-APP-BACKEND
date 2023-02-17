from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/cargosEventos', methods=['GET'])
def cargosEventos():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/cargosEventos/all', methods=['GET'])
def cargosEventosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM cargosEventos;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/cargosEventos/att', methods=['GET'])
def cargosEventosAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM cargosEventos;')
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

@app.route('/cargosEventos/describe', methods=['GET'])
def cargosEventosDescribe():
    if 'idCargoEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idCargoEvento = request.args['idCargoEvento']
    conn = mysqlConnection()
    query = "SELECT * FROM cargosEventos where idCargoEvento = '"+idCargoEvento+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/cargosEventos/insert', methods=['GET'])
def cargosEventosInsert():
    if 'idCargoEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idCargoEvento = request.args['idCargoEvento']
    nome = request.args['nome']
    descricao = request.args['descricao']
    
    conn = mysqlConnection()
    query = "INSERT INTO cargosEventos ( idCargoEvento, nome, descricao ) VALUES( '"+idCargoEvento+"', '"+nome+"' , '"+descricao+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/cargosEventos/remove', methods=['GET'])
def cargosEventosRemove():
    if 'idCargoEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idCargoEvento = request.args['idCargoEvento']
    
    conn = mysqlConnection()
    query = "DELETE FROM cargosEventos WHERE idCargoEvento='"+idCargoEvento+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/cargosEventos/update', methods=['GET'])
def cargosEventosUpdate():
    if 'idCargoEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    conn = mysqlConnection()
    idCargoEvento = request.args['idCargoEvento']
    
    if 'nome' not in request.args:
        query = "SELECT nome FROM cargosEventos WHERE idCargoEvento='"+idCargoEvento+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']

    if 'descricao' not in request.args:
        query = "SELECT descricao FROM cargosEventos WHERE idCargoEvento='"+idCargoEvento+"';"
        records = mysqlQuery(conn, query)
        descricao = str(records[0][0])
    else:
        descricao = request.args['descricao']
    
    query = "UPDATE cargosEventos SET nome='"+nome+"', descricao='"+descricao+"' WHERE idCargoEvento='"+idCargoEvento+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)