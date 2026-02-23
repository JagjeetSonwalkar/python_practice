# 1. Delete a Single Row
cursor.execute("DELETE FROM students WHERE name = 'Alice'")
mysql_connection.commit()

# 2. Delete Multiple Rows Using a Condition
cursor.execute("DELETE FROM students WHERE age < 23")
mysql_connection.commit()

# 3. Delete Using Parameterized Query
query = "DELETE FROM students WHERE name = %s"
data = ("Bob",)
cursor.execute(query, data)
mysql_connection.commit()

# 4. Delete Multiple Rows Using executemany()
query = "DELETE FROM students WHERE name = %s"
data = [("Charlie",), ("David",), ("Eva",)]
cursor.executemany(query, data)
mysql_connection.commit()

# 5. Delete All Rows
cursor.execute("DELETE FROM students")
mysql_connection.commit()

# 6. Delete Using Conditions with AND / OR / LIKE
cursor.execute("DELETE FROM students WHERE age < 25 AND name LIKE 'C%'")
mysql_connection.commit()