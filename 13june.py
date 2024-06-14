import sqlite3 as sql

conn = sql.connect('User.db')
cursor = conn.cursor()

print("Connected to the database")

# sql_command = '''
# CREATE TABLE user( 
# UID INTEGER PRIMARY KEY, 
# username VARCHAR(20), 
# password VARCHAR(30), 
# gender VARCHAR(10));
# '''
# cursor.execute(sql_command)

pk = [1, 3, 4, 5, 6]
username = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']
passw = ['abc']
gender = ['Not defined']
for i in range(5):
    # This is the q-mark style:
    cursor.execute('INSERT INTO user VALUES (?, ?, ?, ?)', (pk[i], username[i], passw[0], gender[0]))


print('Value inserted')
conn.commit()
# close the connection
conn.close()