# Create Cursor (Mandatory for Queries)
# Cursor is used to execute SQL queries.

import mysql.connector

def main():
    connect_mysql = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        database = 'mydb',
        password = 'Jaggi@2510',
    )

    if connect_mysql.is_connected():
        print("Connection successfull with DB")
    else:
        print("Unable to connect with DB")
    
    cursor = connect_mysql.cursor()

    cursor.execute('Select * from employees')
    records = cursor.fetchall()

    for row in records:
        print(row)

if __name__ == "__main__":
    main()