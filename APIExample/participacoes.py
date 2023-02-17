from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/participacoes', methods=['GET'])
def participacoes():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/participacoes/all', methods=['GET'])
def participacoesAll():
    conn = mysqlConnection()
    query = "SELECT * FROM participacoes;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/participacoes/att', methods=['GET'])
def participacoesAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM participacoes;')
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

@app.route('/participacoes/describe', methods=['GET'])
def participacoesDescribe():
    conn = mysqlConnection()
    if 'idEvento' not in request.args and 'email' not in request.args:
        return "Error: No idEvento and email fields provided."
    elif 'idEvento' not in request.args:
        return "Error: No idEvento field provided. Please specify an id."
    elif 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    idEvento = request.args['idEvento']
    email = request.args['email']
    query = "SELECT * FROM participacoes WHERE idEvento = '"+idEvento+"' AND email='"+email+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/participacoes/insert', methods=['GET'])
def participacoesInsert():
    conn = mysqlConnection()
    if 'idEvento' not in request.args and 'email' not in request.args:
        return "Error: No idEvento and email fields provided."
    elif 'idEvento' not in request.args:
        return "Error: No idEvento field provided. Please specify an id."
    elif 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    idEvento = request.args['idEvento']
    email = request.args['email']
    dataInscricao = request.args['dataInscricao']
    
    query = "INSERT INTO participacoes ( idEvento, email, dataInscricao ) VALUES( '"+idEvento+"', '"+email+"', '"+dataInscricao+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/participacoes/remove', methods=['GET'])
def participacoesRemove():
    conn = mysqlConnection()
    if 'idEvento' not in request.args and 'email' not in request.args:
        return "Error: No idEvento and email fields provided."
    elif 'idEvento' not in request.args:
        return "Error: No idEvento field provided. Please specify an id."
    elif 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    idEvento = request.args['idEvento']
    email = request.args['email']

    query = "DELETE FROM participacoes WHERE idEvento='"+idEvento+"' AND email='"+email+"';"
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/participacoes/update', methods=['GET'])
def participacoesUpdate():
    conn = mysqlConnection()
    if 'idEvento' not in request.args and 'email' not in request.args:
        return "Error: No idEvento and email fields provided."
    elif 'idEvento' not in request.args:
        return "Error: No idEvento field provided. Please specify an id."
    elif 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    idEvento = request.args['idEvento']
    email = request.args['email']
    
    if 'dataInscricao' not in request.args:
        query = "SELECT dataInscricao FROM participacoes WHERE idEvento='"+idEvento+"' AND email='"+email+"';"
        records = mysqlQuery(conn, query)
        dataInscricao = str(records[0][0])
    else:
        dataInscricao = request.args['dataInscricao']
    
    query = "UPDATE participacoes SET dataInscricao='"+dataInscricao+"' WHERE idEvento='"+idEvento+"' AND email='"+email+"';"

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)