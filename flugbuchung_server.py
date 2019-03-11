from flask import Flask, render_template
app = Flask(__name__)


@app.route("/signUp")
def sign_up():
    return render_template("sign_up.html")


@app.route("/logIn")
def log_in():
    return render_template("log_in.html")


@app.route("/chooseDate")
def choose_date():
    return render_template("choose_date.html")


@app.route("/bookFlight")
def book_flight():
    return render_template("book_flight.html")


if __name__ == "__main__":
    app.run()

