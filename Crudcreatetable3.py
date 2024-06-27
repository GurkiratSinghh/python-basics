import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)
c=db.cursor()
query="""create table employee(
    emp_id int primary key,
    emp_name varchar(30) not null,
    department varchar(30) not null,
    salary int not null)"""

c.execute(query)
# fetch tblemployee details in the database
c.execute("describe employee")
 
# print the table details
for i in c:
    print(i)
 
#c.execute(query)
db.close()