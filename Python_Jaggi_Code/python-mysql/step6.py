# 1. Update Single Row
cursor.execute("UPDATE students SET age = 24 WHERE name = 'Alice'")
mysql_connection.commit()

# 2. Update Multiple Rows
cursor.execute("UPDATE students SET age = age + 1 WHERE age < 25")
mysql_connection.commit()

# 3. Update Using Parameterized Query
query = "UPDATE students SET age = %s WHERE name = %s"
data = (26, "Bob")
cursor.execute(query, data)
mysql_connection.commit()

# 4. Update Multiple Rows Using executemany()
query = "UPDATE students SET age = %s WHERE name = %s"
data = [
    (27, "Charlie"),
    (28, "David"),
    (23, "Eva")
]
cursor.executemany(query, data)
mysql_connection.commit()

# 5. Update Using Conditions
cursor.execute("UPDATE students SET age = 30 WHERE age < 25 AND name LIKE 'C%'")
mysql_connection.commit()

# 6. Update All Rows
cursor.execute("UPDATE students SET age = 20")
mysql_connection.commit()