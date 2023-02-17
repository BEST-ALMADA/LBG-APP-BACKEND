from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/empresas', methods=['GET'])
def empresas():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/empresas/all', methods=['GET'])
def empresasAll():
    conn = mysqlConnection()
    query = "SELECT * FROM empresas;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/empresas/att', methods=['GET'])
def empresasAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM empresas;')
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

@app.route('/empresas/describe', methods=['GET'])
def empresasDescribe():
    if 'idEmpresa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEmpresa = request.args['idEmpresa']
    conn = mysqlConnection()
    query = "SELECT * FROM empresas where idEmpresa = '"+idEmpresa+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/empresas/insert', methods=['GET'])
def empresasInsert():
    if 'idEmpresa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEmpresa = request.args['idEmpresa']
    nome = request.args['nome']
    dinheiroFinanciado = request.args['dinheiroFinanciado']
    categoria = request.args['categoria']
    
    conn = mysqlConnection()
    query = "INSERT INTO empresas ( idEmpresa, nome, dinheiroFinanciado, categoria ) VALUES( '"+idEmpresa+"', '"+nome+"', '"+dinheiroFinanciado+"', '"+categoria+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/empresas/remove', methods=['GET'])
def empresasRemove():
    if 'idEmpresa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEmpresa = request.args['idEmpresa']
    
    conn = mysqlConnection()
    query = "DELETE FROM empresas WHERE idEmpresa='"+idEmpresa+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/empresas/update', methods=['GET'])
def empresasUpdate():
    if 'idEmpresa' not in request.args:
        return "Error: No id field provided. Please specify an id."

    conn = mysqlConnection()
    idEmpresa = request.args['idEmpresa']
    
    if 'nome' not in request.args:
        query = "SELECT nome FROM empresas WHERE idEmpresa='"+idEmpresa+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']

    if 'dinheiroFinanciado' not in request.args:
        query = "SELECT dinheiroFinanciado FROM empresas WHERE idEmpresa='"+idEmpresa+"';"
        records = mysqlQuery(conn, query)
        dinheiroFinanciado = str(records[0][0])
    else:
        dinheiroFinanciado = request.args['dinheiroFinanciado']

    if 'categoria' not in request.args:
        query = "SELECT categoria FROM empresas WHERE idEmpresa='"+idEmpresa+"';"
        records = mysqlQuery(conn, query)
        categoria = str(records[0][0])
    else:
        categoria = request.args['categoria']
    
    query = "UPDATE empresas SET nome='"+nome+"', dinheiroFinanciado='"+dinheiroFinanciado+"', categoria='"+categoria+"' WHERE idEmpresa='"+idEmpresa+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)