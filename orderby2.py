import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="select * from employee order by emp_name desc"

c.execute(query)

myresult=c.fetchall()
for i in myresult:
    print(i)

db.commit()
db.close()