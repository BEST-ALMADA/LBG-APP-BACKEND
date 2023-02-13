from flask import request, jsonify
from mysqlAccess import mysqlConnection, mysqlCloseConnection, mysqlQuery
from configApp import app
import pessoas




@app.route('/', methods=['GET'])
def home():
    conn = mysqlConnection()
    query = "SHOW TABLES;"
    records = mysqlQuery(conn, query)
    mysqlCloseConnection(conn)
    print(records)
    return jsonify(records)





app.run()