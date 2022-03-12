import mysql.connector

DB = mysql.connector.connect(
    host='localhost',
    user='sele',
    password='',
    database='productos',
    port=3306  
)
