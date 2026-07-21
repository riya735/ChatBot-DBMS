import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='riyamysql2025!',
    database='project'
)

print('hello')

if conn.is_connected():
    print("✅ Connected to MySQL successfully!")

cursor = conn.cursor()

query = """
INSERT INTO Student(StudentID, Name, CGPA)
VALUES (%s, %s, %s)
"""

values = (1, "Riya", 9.51)

cursor.execute(query, values)

conn.commit()

print("1 record inserted.")

cursor.execute("SELECT * FROM Student")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
