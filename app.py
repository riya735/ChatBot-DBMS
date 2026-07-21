from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    print("Request Method:", request.method)

    question = ""
    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        # For now, pretend this is the chatbot answer
        answer = "You asked: " + question

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)
