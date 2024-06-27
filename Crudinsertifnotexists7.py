import mysql.connector as mc

# Connect to the database
db = mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c = db.cursor()

# Fetch and print all records before insertion
c.execute("SELECT * FROM employee")
myresult = c.fetchall()
for i in myresult:
    print(i)

# Insert a record if it does not already exist
query = """
INSERT INTO employee (emp_id, emp_name, department, salary)
SELECT 3, 'Nav', 'Sales', 1500000
WHERE NOT EXISTS (SELECT emp_id FROM employee WHERE emp_id = 3)
"""

# Execute the insertion query
c.execute(query)

# Commit the transaction
db.commit()

# Fetch and print all records after insertion
print("After inserting a record....")
c.execute("SELECT * FROM employee")
myresult = c.fetchall()
for i in myresult:
    print(i)

# Close the connection
db.close()
