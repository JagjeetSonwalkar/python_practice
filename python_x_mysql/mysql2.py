# connect with database

import mysql.connector

def main():
    connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Jaggi@2510',
        database = 'mydb'
    )

    if connect.is_connected():
        print("Database is connected successfully")
    else:
        print("Unable to connect with database")

if __name__ == "__main__":
    main()