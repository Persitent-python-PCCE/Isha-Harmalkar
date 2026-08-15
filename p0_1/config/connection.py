import mysql.connector


def getConnection():
    try:
        user = 'root'
        password = 'password'
        host = '127.0.0.1'
        database = 'p_01'

        conn = mysql.connector.connect(host=host, user=user, password=password,database=database)
        print("Connected to db successfully.")
        return conn
    except Exception as err:
        print("Sql Connection error: ", err)
        return None
