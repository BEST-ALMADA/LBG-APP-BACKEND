from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/membros', methods=['GET'])
def membros():
    accessPoints = ["all", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/membros/all', methods=['GET'])
def membrosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM membros;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/membros/att', methods=['GET'])
def eventosAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM membros;')
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

@app.route('/membros/describe', methods=['GET'])
def membrosDescribe():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    email = request.args['email']
    conn = mysqlConnection()
    query = "SELECT * FROM membros where email = '"+email+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/membros/insert', methods=['GET'])
def membrosInsert():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    email = request.args['email']
    membership = request.args['membership']
    dataEntrada = request.args['dataEntrada']
    tempoLBGSemestres = request.args['tempoLBGSemestres']
    foto = request.args['foto']
    
    conn = mysqlConnection()
    query = "INSERT INTO membros ( email, membership, dataEntrada, tempoLBGSemestres, foto ) VALUES( '"+email+"', '"+membership+"', '"+dataEntrada+"', '"+tempoLBGSemestres+"', '"+foto+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/membros/remove', methods=['GET'])
def membrosRemove():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    email = request.args['email']
    
    conn = mysqlConnection()
    query = "DELETE FROM membros WHERE email='"+email+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/membros/update', methods=['GET'])
def membrosUpdate():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    conn = mysqlConnection()
    email = request.args['email']
    
    if 'membership' not in request.args:
        query = "SELECT membership FROM membros WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        membership = str(records[0][0])
    else:
        membership = request.args['membership']

    if 'dataEntrada' not in request.args:
        query = "SELECT dataEntrada FROM membros WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        dataEntrada = str(records[0][0])
    else:
        dataEntrada = request.args['dataEntrada']

    if 'tempoLBGSemestres' not in request.args:
        query = "SELECT tempoLBGSemestres FROM membros WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        tempoLBGSemestres = str(records[0][0])
    else:
        tempoLBGSemestres = request.args['tempoLBGSemestres']

    if 'foto' not in request.args:
        query = "SELECT foto FROM membros WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        foto = str(records[0][0])
    else:
        foto = request.args['foto']
    
    query = "UPDATE membros SET membership='"+membership+"', dataEntrada='"+dataEntrada+"', tempoLBGSemestres='"+tempoLBGSemestres+"', foto='"+foto+"' WHERE email='"+email+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)