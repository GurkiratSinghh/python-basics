#Count SQL Table Column Using Python
import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27",
    database="employee_db"
)

c=db.cursor()
query="""desc  employees"""

c.execute(query)
column=c.fetchall()
count=len(column)
print(count)

db.close()
