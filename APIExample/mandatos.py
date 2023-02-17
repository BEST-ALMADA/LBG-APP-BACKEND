from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/mandatos', methods=['GET'])
def mandatos():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/mandatos/all', methods=['GET'])
def mandatosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM mandatos;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/mandatos/att', methods=['GET'])
def mandatosAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM mandatos;')
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

@app.route('/mandatos/describe', methods=['GET'])
def mandatosDescribe():
    conn = mysqlConnection()

    idCargo = request.args.get('idCargo')
    email = request.args.get('email')
    dataInicio = request.args.get('dataInicio')

    if not all((idCargo, email, dataInicio)):
        if not idCargo:
            return "Error: No idCargo field provided."
        elif not email:
            return "Error: No email field provided."
        elif not dataInicio:
            return "Error: No dataInicio field provided."
        else:
            return "Error: No idCargo, email and dataInicio fields provided."

    query = f"SELECT * FROM mandatos WHERE idCargo='{idCargo}' AND email='{email}' AND dataInicio='{dataInicio}';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/mandatos/insert', methods=['GET'])
def mandatosInsert():
    conn = mysqlConnection()

    idCargo = request.args.get('idCargo')
    email = request.args.get('email')
    dataInicio = request.args.get('dataInicio')

    if not all((idCargo, email, dataInicio)):
        if not idCargo:
            return "Error: No idCargo field provided."
        elif not email:
            return "Error: No email field provided."
        elif not dataInicio:
            return "Error: No dataInicio field provided."
        else:
            return "Error: No idCargo, email and dataInicio fields provided."

    dataFim = request.args['dataFim']

    query = "INSERT INTO mandatos ( idCargo, email, dataInicio, dataFim ) VALUES( '"+idCargo+"', '"+email+"', '"+dataInicio+"', '"+dataFim+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/mandatos/remove', methods=['GET'])
def mandatosRemove():
    conn = mysqlConnection()

    idCargo = request.args.get('idCargo')
    email = request.args.get('email')
    dataInicio = request.args.get('dataInicio')

    if not all((idCargo, email, dataInicio)):
        if not idCargo:
            return "Error: No idCargo field provided."
        elif not email:
            return "Error: No email field provided."
        elif not dataInicio:
            return "Error: No dataInicio field provided."
        else:
            return "Error: No idCargo, email and dataInicio fields provided."

    query = f"DELETE FROM mandatos WHERE idCargo='{idCargo}' AND email='{email}' AND dataInicio='{dataInicio}';"
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/mandatos/update', methods=['GET'])
def mandatosUpdate():
    conn = mysqlConnection()

    idCargo = request.args.get('idCargo')
    email = request.args.get('email')
    dataInicio = request.args.get('dataInicio')

    if not all((idCargo, email, dataInicio)):
        if not idCargo and not email:
            return "Error: No idCargo and email fields provided."
        elif not idCargo and not dataInicio:
            return "Error: No idCargo and dataInicio fields provided."
        elif not email and not dataInicio:
            return "Error: No email and dataInicio fields provided."
        elif not idCargo:
            return "Error: No idCargo field provided."
        elif not email:
            return "Error: No email field provided."
        elif not dataInicio:
            return "Error: No dataInicio field provided."
        else:
            return "Error: No idCargo, email and dataInicio fields provided."

    dataFim = request.args['dataFim']

    if 'dataFim' not in request.args:
        query = f"SELECT dataFim FROM mandatos WHERE idCargo='{idCargo}' AND email='{email}' AND dataInicio='{dataInicio}';"
        records = mysqlQuery(conn, query)
        dataFim = str(records[0][0])
    else:
        dataFim = request.args['dataFim']
    
    query = "UPDATE mandatos SET dataFim='"+dataFim+"' WHERE idCargo='{idCargo}' AND email='{email}' AND dataInicio='{dataInicio}';"
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)