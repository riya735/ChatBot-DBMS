from flask import Flask, render_template, request
from main import cursor
from llm import generate_sql

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    question = ""
    answer = []
    sql = ""

    if request.method == "POST":

        question = request.form["question"]

        sql = generate_sql(question)

        print("Generated SQL:")
        print(sql)

        if sql.lower().startswith("select"):

            try:

                cursor.execute(sql)

                answer = cursor.fetchall()

            except Exception as e:

                answer = str(e)

        else:

            answer = "Only SELECT queries are allowed."

    return render_template(
        "index.html",
        question=question,
        answer=answer,
        sql=sql
    )

if __name__ == "__main__":
    app.run(debug=True)

