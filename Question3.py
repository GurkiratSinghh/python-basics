#How to Add a Column to a MySQL Table in Python?
import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="""alter table employees add column bonus int"""

c.execute(query)

db.close()