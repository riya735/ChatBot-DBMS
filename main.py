import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='chatbot_db'
)

cursor = conn.cursor()
