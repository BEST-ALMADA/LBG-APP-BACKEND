from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/eventos', methods=['GET'])
def eventos():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/eventos/all', methods=['GET'])
def eventosAll():
    conn = mysqlConnection()
    query = "SELECT * FROM eventos;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/eventos/att', methods=['GET'])
def eventosAtt_new():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM eventos;')
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

@app.route('/eventos/describe', methods=['GET'])
def eventosDescribe():
    if 'idEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEvento = request.args['idEvento']
    conn = mysqlConnection()
    query = "SELECT * FROM eventos where idEvento = '"+idEvento+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/eventos/insert', methods=['GET'])
def eventosInsert():
    if 'idEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEvento = request.args['idEvento']
    idEquipaEvento = request.args['idEquipaEvento']
    nome = request.args['nome']
    descricao = request.args['descricao']
    numTotalParticipantes = request.args['numTotalParticipantes']
    numAtualParticipantes = request.args['numAtualParticipantes']
    dataInicio = request.args['dataInicio']
    dataFim = request.args['dataFim']
    sponsors = request.args['sponsors']
    contactosCoordenacao = request.args['contactosCoordenacao']
    
    conn = mysqlConnection()
    query = "INSERT INTO eventos ( idEvento, idEquipaEvento, nome, descricao, numTotalParticipantes, numAtualParticipantes, dataInicio, dataFim, sponsors, contactosCoordenacao ) VALUES( '"+idEvento+"', '"+idEquipaEvento+"' , '"+nome+"', '"+descricao+"', '"+numTotalParticipantes+"', '"+numAtualParticipantes+"', '"+dataInicio+"', '"+dataFim+"', '"+sponsors+"', '"+contactosCoordenacao+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/eventos/remove', methods=['GET'])
def eventosRemove():
    if 'idEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    idEvento = request.args['idEvento']
    
    conn = mysqlConnection()
    query = "DELETE FROM eventos WHERE idEvento='"+idEvento+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/eventos/update', methods=['GET'])
def eventosUpdate():
    if 'idEvento' not in request.args:
        return "Error: No id field provided. Please specify an id."

    conn = mysqlConnection()
    idEvento = request.args['idEvento']
    
    if 'idEquipaEvento' not in request.args:
        query = "SELECT idEquipaEvento FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        idEquipaEvento = str(records[0][0])
    else:
        idEquipaEvento = request.args['idEquipaEvento']

    if 'nome' not in request.args:
        query = "SELECT nome FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']

    if 'descricao' not in request.args:
        query = "SELECT descricao FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        descricao = str(records[0][0])
    else:
        descricao = request.args['descricao']

    if 'numTotalParticipantes' not in request.args:
        query = "SELECT numTotalParticipantes FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        numTotalParticipantes = str(records[0][0])
    else:
        numTotalParticipantes = request.args['numTotalParticipantes']

    if 'numAtualParticipantes' not in request.args:
        query = "SELECT numAtualParticipantes FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        numAtualParticipantes = str(records[0][0])
    else:
        numAtualParticipantes = request.args['numAtualParticipantes']
    
    if 'dataInicio' not in request.args:
        query = "SELECT dataInicio FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        dataInicio = str(records[0][0])
    else:
        dataInicio = request.args['dataInicio']

    if 'dataFim' not in request.args:
        query = "SELECT dataFim FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        dataFim = str(records[0][0])
    else:
        dataFim = request.args['dataFim']

    if 'sponsors' not in request.args:
        query = "SELECT sponsors FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        sponsors = str(records[0][0])
    else:
        sponsors = request.args['sponsors']
    
    if 'contactosCoordenacao' not in request.args:
        query = "SELECT contactosCoordenacao FROM eventos WHERE idEvento='"+idEvento+"';"
        records = mysqlQuery(conn, query)
        contactosCoordenacao = str(records[0][0])
    else:
        contactosCoordenacao = request.args['contactosCoordenacao']
    
    query = "UPDATE eventos SET idEquipaEvento='"+idEquipaEvento+"', nome='"+nome+"', descricao='"+descricao+"', numTotalParticipantes='"+numTotalParticipantes+"', numAtualParticipantes='"+numAtualParticipantes+"', dataInicio='"+dataInicio+"', dataFim='"+dataFim+"', sponsors='"+sponsors+"', contactosCoordenacao='"+contactosCoordenacao+"' WHERE idEvento='"+idEvento+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)