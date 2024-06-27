import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()

query="""insert into employee(emp_id,
    emp_name ,department,salary) values(%s,%s,%s,%s)"""
data=[(1,"Kirat","HR",1900000),
    (2,"Nav","Sales",1500000),
    (3,"Raman","Marketing",1700000),
    (4,"Kulwinder","Manager",2500000)]

c.executemany(query,data)
db.commit()
db.close()