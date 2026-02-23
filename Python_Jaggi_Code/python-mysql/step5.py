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

    # create cursor: Using Dictionary Cursor
    cursor = main_connection.cursor(dictionary=True)

    # read data
    cursor.execute("select * from mydetails")
    rows = cursor.fetchall()
    for r in rows:
        print(r)

    # Filtering Data Using WHERE Clause
    cursor.execute("select * from mydetails where age > 20")
    rows = cursor.fetchall()
    for r in rows:
        print(r)

else:
    print("Unable to connection with mysql!!")

main_connection.close()