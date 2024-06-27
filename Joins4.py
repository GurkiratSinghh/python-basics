import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="select emp_id,emp_name, department ,Project from employee right join products on employee.emp_id= products.p_id "

c.execute(query)

myresult=c.fetchall()
for i in myresult:
    print(i)

db.commit()
db.close()