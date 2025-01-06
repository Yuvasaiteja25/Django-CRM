import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='tiger'
)

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("ALL done") 