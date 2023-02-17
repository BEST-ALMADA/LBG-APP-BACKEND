from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/documentos', methods=['GET'])
def documentos():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/documentos/all', methods=['GET'])
def documentosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM documentos;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/documentos/att', methods=['GET'])
def documentosAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM documentos;')
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

@app.route('/documentos/describe', methods=['GET'])
def documentosDescribe():
    if 'idDocumento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idDocumento = request.args['idDocumento']
    conn = mysqlConnection()
    query = "SELECT * FROM documentos where idDocumento = '"+idDocumento+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/documentos/insert', methods=['GET'])
def documentosInsert():
    if 'idDocumento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idDocumento = request.args['idDocumento']
    tipo = request.args['tipo']
    nome = request.args['nome']
    descricao = request.args['descricao']
    dataCriacao = request.args['dataCriacao']
    localizacao = request.args['localizacao']
    
    conn = mysqlConnection()
    query = "INSERT INTO documentos ( idDocumento, tipo, nome, descricao, dataCriacao, localizacao ) VALUES( '"+idDocumento+"', '"+tipo+"', '"+nome+"', '"+descricao+"', '"+dataCriacao+"', '"+localizacao+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/documentos/remove', methods=['GET'])
def documentosRemove():
    if 'idDocumento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idDocumento = request.args['idDocumento']
    
    conn = mysqlConnection()
    query = "DELETE FROM documentos WHERE idDocumento='"+idDocumento+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/documentos/update', methods=['GET'])
def documentosUpdate():
    if 'idDocumento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    conn = mysqlConnection()
    idDocumento = request.args['idDocumento']
    
    if 'tipo' not in request.args:
        query = "SELECT tipo FROM documentos WHERE idDocumento='"+idDocumento+"';"
        records = mysqlQuery(conn, query)
        tipo = str(records[0][0])
    else:
        tipo = request.args['tipo']

    if 'nome' not in request.args:
        query = "SELECT nome FROM documentos WHERE idDocumento='"+idDocumento+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']

    if 'descricao' not in request.args:
        query = "SELECT descricao FROM documentos WHERE idDocumento='"+idDocumento+"';"
        records = mysqlQuery(conn, query)
        descricao = str(records[0][0])
    else:
        descricao = request.args['descricao']

    if 'dataCriacao' not in request.args:
        query = "SELECT dataCriacao FROM documentos WHERE idDocumento='"+idDocumento+"';"
        records = mysqlQuery(conn, query)
        dataCriacao = str(records[0][0])
    else:
        dataCriacao = request.args['dataCriacao']

    if 'localizacao' not in request.args:
        query = "SELECT localizacao FROM documentos WHERE idDocumento='"+idDocumento+"';"
        records = mysqlQuery(conn, query)
        localizacao = str(records[0][0])
    else:
        localizacao = request.args['localizacao']
    
    query = "UPDATE documentos SET tipo='"+tipo+"', nome='"+nome+"', descricao='"+descricao+"', dataCriacao='"+dataCriacao+"', localizacao='"+localizacao+"' WHERE idDocumento='"+idDocumento+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)