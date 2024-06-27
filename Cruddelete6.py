import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="delete from employee where emp_id=2"
c.execute(query)
db.commit()
db.close()