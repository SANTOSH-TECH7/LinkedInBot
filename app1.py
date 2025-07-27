from flask import Flask, render_template, request
from linkedin_hr_bot import run_bot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        keyword = request.form["keyword"]
        message = run_bot(username, password, keyword)
    return render_template("index.html", result=message)

if __name__ == "__main__":
    app.run(debug=True)
