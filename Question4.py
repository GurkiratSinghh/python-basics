#How to Get the Minimum and maximum Value of a Column of a MySQL Table Using Python?
import mysql.connector as mc
dataBase=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

cursorObject=dataBase.cursor()

query="select min(salary) ,max(emp_id) from employees "

cursorObject.execute(query)

myresult=cursorObject.fetchall()
for i in myresult:
    print(i)
    
dataBase.close()