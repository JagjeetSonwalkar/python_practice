import mysql.connector

def main():
    p = input("Enter the password of database: ")

    main_connecction = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = p,
        database = "company"
    )

    if main_connecction.is_connected():
        print("connected with mysql.")

        try:
            cursor = main_connecction.cursor()

            cursor.execute("select * from mydetails")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            #   main_connecction.commit()
        
        except mysql.connector.Error as e:
            print("ERROR",e)
            main_connecction.rollback()
        
        finally:
            cursor.close()
            main_connecction.close()

    else:
        print("unable to connect with mysql")

if __name__ == "__main__":
    main()

'''
Best Practices
Always use parameterized queries to prevent SQL injection.
Always commit changes after INSERT, UPDATE, DELETE.
Always close cursor and connection.
Use try-except blocks for error handling
'''