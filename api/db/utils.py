'''
Connection functions to create session with db
'''
import mysql.connector


def db_init():
    mydb = mysql.connector.connect(
        host='mysqldb',
        user='root',
        password='p@ssw0rd1',
        database='madness'
    )
    cursor = mydb.cursor()

    cursor.execute()

