#How to Perform Arithmetic Across Columns of a MySQL Table Using Python?
import mysql.connector as mc

# Establish a database connection
dataBase = mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

# Create a cursor object
cursorObject = dataBase.cursor()

print("Displaying Data from Employee_db")
query = "SELECT bonus, salary, (bonus + salary) AS total_amount FROM employees"

cursorObject.execute(query)

myresult = cursorObject.fetchall()
for row in myresult:
    print(row)

# Close the database connection
dataBase.close()
