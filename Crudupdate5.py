import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="update  employee set salary=2200000 where emp_id=1"

c.execute(query)
print(c.rowcount,"row updated")
db.commit()
db.close()