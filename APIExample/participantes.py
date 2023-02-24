from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/participantes', methods=['GET'])
def participantes():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/participantes/all', methods=['GET'])
def participantesAll():
    conn = mysqlConnection()
    query = "SELECT * FROM participantes;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/participantes/att', methods=['GET'])
def participantesAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM participantes;')
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

@app.route('/participantes/describe', methods=['GET'])
def participantesDescribe():
    conn = mysqlConnection()

    if 'email' not in request.args:
        return "Error: No email field provided."
    
    email = request.args.get('email')

    query = f"SELECT * FROM participantes WHERE email='{email}';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/participantes/insert', methods=['GET'])
def participantesInsert():
    conn = mysqlConnection()

    if 'email' not in request.args:
        return "Error: No email field provided."
    
    email = request.args.get('email')
    dataExpiracaoDoc = request.args['dataExpiracaoDoc']
    contactoEmerg = request.args['contactoEmerg']
    dieta = request.args['dieta']
    ultimaDataLogin = request.args['ultimaDataLogin']

    query = "INSERT INTO participantes ( email, dataExpiracaoDoc, contactoEmerg, dieta, ultimaDataLogin ) VALUES( '"+email+"', '"+dataExpiracaoDoc+"', '"+contactoEmerg+"', '"+dieta+"', '"+ultimaDataLogin+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/participantes/remove', methods=['GET'])
def participantesRemove():
    conn = mysqlConnection()

    if 'email' not in request.args:
        return "Error: No email field provided."
    
    email = request.args.get('email')

    query = f"DELETE FROM participantes WHERE email='{email}';"
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/participantes/update', methods=['GET'])
def participantesUpdate():
    conn = mysqlConnection()

    if 'email' not in request.args:
        return "Error: No email field provided."
    
    email = request.args.get('email')
    dataExpiracaoDoc = request.args['dataExpiracaoDoc']
    contactoEmerg = request.args['contactoEmerg']
    dieta = request.args['dieta']
    ultimaDataLogin = request.args['ultimaDataLogin']

    if 'dataExpiracaoDoc' not in request.args:
        query = f"SELECT dataExpiracaoDoc FROM participantes WHERE email='{email}';"
        records = mysqlQuery(conn, query)
        dataExpiracaoDoc = str(records[0][0])
    else:
        dataExpiracaoDoc = request.args['dataExpiracaoDoc']

    if 'contactoEmerg' not in request.args:
        query = f"SELECT contactoEmerg FROM participantes WHERE email='{email}';"
        records = mysqlQuery(conn, query)
        contactoEmerg = str(records[0][0])
    else:
        contactoEmerg = request.args['contactoEmerg']

    if 'dieta' not in request.args:
        query = f"SELECT dieta FROM participantes WHERE email='{email}';"
        records = mysqlQuery(conn, query)
        dieta = str(records[0][0])
    else:
        dieta = request.args['dieta']

    if 'ultimaDataLogin' not in request.args:
        query = f"SELECT ultimaDataLogin FROM participantes WHERE email='{email}';"
        records = mysqlQuery(conn, query)
        ultimaDataLogin = str(records[0][0])
    else:
        ultimaDataLogin = request.args['ultimaDataLogin']

    query = f"UPDATE participantes SET dataExpiracaoDoc='"+dataExpiracaoDoc+"', contactoEmerg='"+contactoEmerg+"', dieta='"+dieta+"', ultimaDataLogin='"+ultimaDataLogin+"' WHERE email='"+email+"';"
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)