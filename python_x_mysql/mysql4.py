# create db if not exists

import mysql.connector

# varibale
database_name = 'testdb'

def main():
    connect_mysql = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Jaggi@2510',
    )

    if connect_mysql.is_connected():
        print("Connection successfull with DB")

        cursor = connect_mysql.cursor()

        query = '''
select schema_name
from information_schema.schemata
where schema_name = %s
        '''

        cursor.execute(query, (database_name,))

        result = cursor.fetchone()

        if result:
            print("DB exists")
        else:
            print("DB not exists!!")

            print(f"Creating new data base with name {database_name}")

            query = f'create database {database_name}'

            cursor.execute(query)

            result = cursor.fetchone()

            print("Created data base succesfully")
            
    else:
        print("Unable to connect with DB")

    cursor.close()
    connect_mysql.close()
    

if __name__ == "__main__":
    main()