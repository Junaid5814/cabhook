import mysql.connector

cnx = mysql.connector.connect(
    host="sql12.freemysqlhosting.net",
    user="sql12595354",
    password="FhrtwRn45l",
    database="sql12595354",
    port=3306
)

if cnx.is_connected():
    print("Connection to the database is established and active.")
else:
    print("Connection to the database is not active.")