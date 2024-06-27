import mysql.connector as mc
dataBase=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

cursorObject=dataBase.cursor()

print("Displaying Data from Employee_db")
query="select * from employees"

cursorObject.execute(query)

myresult=cursorObject.fetchall()
for i in myresult:
    print(i)
    
dataBase.close()