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

    # insert data
    '''
    cursor.execute("insert into mydetails (name, age) values (%s, %s)", ("Rohit",45))
    main_connection.commit()
    '''

    '''
    query = "insert into mydetails (name, age) values (%s, %s)"
    data = ("Virat", 18)
    cursor.execute(query, data)
    main_connection.commit() 
    ''' 

    query = "insert into mydetails (name, age) values (%s, %s)"
    data = [
        ("Hardik", 33),
        ("Ishan", 15),
        ("Bumrha", 1)
        ]
    cursor.executemany(query, data)
    main_connection.commit() 

else:
    print("Unable to connection with mysql!!")

main_connection.close()