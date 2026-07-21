from flask import Flask, render_template, request
from main import cursor

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    answer = None

    if request.method == "POST": 
        question = request.form.get("question", "").lower() 
        
        if "student" in question: 
            cursor.execute("SELECT * FROM Student") 
            answer = cursor.fetchall() 
        elif "course" in question: 
            cursor.execute("SELECT * FROM Course") 
            answer = cursor.fetchall() 
        elif "enrollment" in question: 
            cursor.execute("SELECT * FROM Enrollment") 
            answer = cursor.fetchall() 
        else: 
            answer = "Sorry, I don't understand the question." 

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)
