#Create a mysql connection
import mysql.connector
from mysql.connector import Error

MYSQL_HOST = "108.143.251.143"
MYSQL_DB = "LBGAPP"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Porca0ntasRemota"

def mysqlConnection():
    #Create a mysql connection
    try:
        conn = mysql.connector.connect(host=MYSQL_HOST,
                                       database=MYSQL_DB,
                                       user=MYSQL_USER,
                                       password=MYSQL_PASSWORD)
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)
        return False

def mysqlCloseConnection(conn):
    #Close a mysql connection
    try:
        conn.close()
        print('Connection closed')
        return True
    except Error as e:
        print(e)
        return False

def mysqlQuery(conn, query):
    #Execute a query
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Error as e:
        print(e)
        return False

def mysqlInsert(conn, query):
    #Execute a query
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def mysqlUpdate(conn, query):
    #Execute a query
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False
