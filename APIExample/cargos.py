from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/cargos', methods=['GET'])
def cargos():
    accessPoints = ["all", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/cargos/all', methods=['GET'])
def cargosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM cargos;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/cargos/att', methods=['GET'])
def cargosAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM cargos;')
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

@app.route('/cargos/describe', methods=['GET'])
def cargosDescribe():
    if 'idCargo' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idCargo = request.args['idCargo']
    conn = mysqlConnection()
    query = "SELECT * FROM cargos where idCargo = '"+idCargo+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/cargos/insert', methods=['GET'])
def cargosInsert():
    if 'idCargo' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idCargo = request.args['idCargo']
    nome = request.args['nome']
    descricao = request.args['descricao']
    
    conn = mysqlConnection()
    query = "INSERT INTO cargos ( idCargo, nome, descricao ) VALUES( '"+idCargo+"', '"+nome+"' , '"+descricao+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/cargos/remove', methods=['GET'])
def cargosRemove():
    if 'idCargo' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idCargo = request.args['idCargo']
    
    conn = mysqlConnection()
    query = "DELETE FROM cargos WHERE idCargo='"+idCargo+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/cargos/update', methods=['GET'])
def cargosUpdate():
    if 'idCargo' not in request.args:
        return "Error: No id field provided. Please specify an id."

    conn = mysqlConnection()
    idCargo = request.args['idCargo']
    
    if 'nome' not in request.args:
        query = "SELECT nome FROM cargos WHERE idCargo='"+idCargo+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']

    if 'descricao' not in request.args:
        query = "SELECT descricao FROM cargos WHERE idCargo='"+idCargo+"';"
        records = mysqlQuery(conn, query)
        descricao = str(records[0][0])
    else:
        descricao = request.args['descricao']
    
    query = "UPDATE cargos SET nome='"+nome+"', descricao='"+descricao+"' WHERE idCargo='"+idCargo+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)