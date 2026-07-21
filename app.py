from flask import Flask, render_template, request
from main import cursor

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    question = ""
    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        cursor.execute("SELECT * FROM Student")
        answer = cursor.fetchall()

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)

