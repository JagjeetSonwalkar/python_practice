# Connecting to MySQL

import mysql.connector

# connection with mysql
# mysql_connection is the active connection/session object that lets your Python code communicate with the MySQL database
mysql_connection = mysql.connector.connect(
    host = "localhost", # server address
    user = "root",      # mysql username
    password = "Jagjeet@2510", # mysql password
    database = "company" # databse name
)

if mysql_connection.is_connected():
    print("Connection successful with mysql")
else:
    print("connection fail with mysql!!")

# create cursor to execute queries
cursor = mysql_connection.cursor()

mysql_connection.close()