import mysql.connector as mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="Gurinder@27"
)
c=db.cursor()
query="Create database employee_db"
#c.execute(query)
c.execute("Show databases")
for i in c:
    print(i)
db.close()