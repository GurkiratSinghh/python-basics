import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="select emp_name from employee where emp_id=1"

c.execute(query)

myresult=c.fetchall()
for i in myresult:
    print(i)

db.commit()
db.close()