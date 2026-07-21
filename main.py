import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='riyamysql2025!',
    database='project'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Student")
print(cursor.fetchall())
