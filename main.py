import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='riyamysql2025!',
    database='project'
)

print('hello')

cursor= conn.cursor()
