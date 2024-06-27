#How to Count the Number of Rows in a MySQL Table in Python?
import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="select count(emp_id) from employees"

c.execute(query)
rows = c.fetchone()

# Get the number of rows
for i in rows:
    print(i)


db.close()

