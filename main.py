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
<<<<<<< HEAD
=======


>>>>>>> 83439acd8ec35104a55ba532f9f76eaf0f38f2e2
