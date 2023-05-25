import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Pass@123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("ALL DONE!!")