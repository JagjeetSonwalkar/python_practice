# execute SQL queries. featch all records

import mysql.connector

def main():
    connectx = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Jaggi@2510',
        database = 'mydb'
    )

    cursor = connectx.cursor()

    if connectx.is_connected():
        print("DB is connected successfully")

        query = input("Enter your query: ").strip().lower()
        cursor.execute(query)

        records = cursor.fetchall()

        for row in records:
            print(row)

    else:
        print("DB is not connected!!")
    

if __name__ == "__main__":
    main()