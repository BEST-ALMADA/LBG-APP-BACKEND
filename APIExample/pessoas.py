from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery, mysqlInsert, mysqlUpdate
from configApp import app

@app.route('/pessoas', methods=['GET'])
def pessoas():
    accessPoints = ["all", "att", "describe", "insert", "remove"]
    return jsonify(accessPoints)

@app.route('/pessoas/all', methods=['GET'])
def pessoasAll():
    conn = mysqlConnection()
    query = "SELECT * FROM pessoas;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/pessoas/att', methods=['GET'])
def pessoasAtt():
    conn = mysqlConnection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM pessoas;')
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

@app.route('/pessoas/describe', methods=['GET'])
def pessoasDescribe():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    email = request.args['email']
    conn = mysqlConnection()
    query = "SELECT * FROM pessoas where email = '"+email+"';"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/pessoas/insert', methods=['GET'])
def pessoasInsert():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    email = request.args['email']
    descricao = request.args['descricao']
    nome = request.args['nome']
    alcunha = request.args['alcunha']
    dataNascimento = request.args['dataNascimento']
    password = request.args['password']
    telemovel = request.args['telemovel']
    tamanho = request.args['tamanho']
    
    conn = mysqlConnection()
    query = "INSERT INTO pessoas ( email, descricao, nome, alcunha, dataNascimento, password, telemovel, tamanho ) VALUES( '"+email+"', '"+descricao+"','"+nome+"' , '"+alcunha+"', '"+dataNascimento+"', '"+password+"', "+telemovel+", '"+tamanho+"' );"
    print(query)
    records = mysqlInsert(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)

@app.route('/pessoas/remove', methods=['GET'])
def pessoasRemove():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    email = request.args['email']
    
    conn = mysqlConnection()
    query = "DELETE FROM pessoas WHERE email='"+email+"';" 
    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)

@app.route('/pessoas/update', methods=['GET'])
def pessoasUpdate():
    if 'email' not in request.args:
        return "Error: No email field provided. Please specify an email."

    conn = mysqlConnection()
    email = request.args['email']

    if 'descricao' not in request.args:
        query = "SELECT descricao FROM pessoas WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        descricao = str(records[0][0])
    else:
        descricao = request.args['descricao']
    
    if 'nome' not in request.args:
        query = "SELECT nome FROM pessoas WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        nome = str(records[0][0])
    else:
        nome = request.args['nome']
    
    if 'alcunha' not in request.args:
        query = "SELECT alcunha FROM pessoas WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        alcunha = str(records[0][0])
    else:
        alcunha = request.args['alcunha']

    if 'dataNascimento' not in request.args:
        query = "SELECT dataNascimento FROM pessoas WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        dataNascimento = str(records[0][0])
    else:
        dataNascimento = request.args['dataNascimento']

    if 'password' not in request.args:
        query = "SELECT password FROM pessoas WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        password = str(records[0][0])
    else:
        password = request.args['password']

    if 'telemovel' not in request.args:
        query = "SELECT telemovel FROM pessoas WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        telemovel = str(records[0][0])
    else:
        telemovel = request.args['telemovel']
    
    if 'tamanho' not in request.args:
        query = "SELECT tamanho FROM pessoas WHERE email='"+email+"';"
        records = mysqlQuery(conn, query)
        tamanho = str(records[0][0])
    else:
        tamanho = request.args['tamanho']
    
    
    query = "UPDATE pessoas SET descricao='"+descricao+"', nome='"+nome+"', alcunha='"+alcunha+"', dataNascimento='"+dataNascimento+"', password='"+password+"', telemovel='"+telemovel+"', tamanho='"+tamanho+"' WHERE email='"+email+"';" 

    records = mysqlUpdate(conn, query)
    mysqlCloseConnection(conn)
    return jsonify(records)