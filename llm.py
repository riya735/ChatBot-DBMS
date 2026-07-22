import ollama

def generate_sql(question):

    prompt = f"""
You are an expert MySQL assistant.

Database Schema:

Student(
    StudentID,
    Name,
    Branch,
    CGPA
)

Course(
    CourseID,
    CourseName,
    Credits
)

Enrollment(
    EnrollmentID,
    StudentID,
    CourseID,
    Grade
)

Rules:
1. Return ONLY SQL.
2. Return ONLY SELECT queries.
3. Do not explain anything.

Question:
{question}
"""

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
