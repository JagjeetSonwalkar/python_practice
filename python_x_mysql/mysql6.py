import mysql.connector


def get_connection():
    return mysql.connector.connect(
        user='root',
        password='Jaggi@2510',
        host='localhost',
        database='mydb'
    )

# global variable
table_name = ''

def set_table_name(new_name):
    global table_name
    table_name = new_name

def get_all():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        for record in records:
            print(record)
    finally:
        cursor.close()
        connection.close()

def get(emp_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = f"SELECT * FROM {table_name} WHERE id = %s"
        cursor.execute(query, (emp_id,))
        record = cursor.fetchone()
        print(record)
    finally:
        cursor.close()
        connection.close()

def put(emp_id, name, department, salary):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = f"""
        INSERT INTO {table_name} (id, name, department, salary)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (emp_id, name, department, salary))
        connection.commit()
        print("Data inserted successfully.")
    finally:
        cursor.close()
        connection.close()

def main():
    set_table_name('employees')

    get_all()
    get(1)
    put(5, 'virat', 'NON IT', 25000)
    get_all()

if __name__ == "__main__":
    main()
