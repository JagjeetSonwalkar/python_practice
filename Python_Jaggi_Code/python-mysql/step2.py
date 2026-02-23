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

    # create table
    cursor.execute("""
    Create table if not exists mydetails(
        id int auto_increment primary key,
        name varchar(25),
        age int not null
    )
    """)

else:
    print("Unable to connection with mysql!!")

main_connection.close()