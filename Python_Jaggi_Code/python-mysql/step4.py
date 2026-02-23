# curd operation

import mysql.connector

main_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Jagjeet@2510",
    database = "company"
)

if main_connection.is_connected():
    print("connected with mysql.")

    # create cursor
    cursor = main_connection.cursor()

    # read data
    cursor.execute("select * from mydetails")

    # Using SELECT and fetchone()
    row = cursor.fetchone()
    print(row)

    # using fetachall()
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    
    # using fetchmany
    rows = cursor.fetchmany(size=3)
    for r in rows:
        print(r)
    
    # Using Loops Directly on Cursor
    for r in cursor:
        print(r)

else:
    print("Unable to connection with mysql!!")


main_connection.close()