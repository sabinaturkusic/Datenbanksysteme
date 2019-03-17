from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)


### Localhost for HTML ###
@app.route("/signUp")
def sign_up():
    return render_template("sign_up.html")
    # add server-db interaction code


@app.route("/logIn")
def log_in():
    return render_template("log_in.html")
# add server-db interaction code
    # read values
    # validate values


@app.route("/chooseDate")
def choose_date():
    return render_template("choose_date.html")
# add server-db interaction code
    # read values
    # validate values


@app.route("/bookFlight")
def book_flight():
    return render_template("book_flight.html")
# add server-db interaction code
    # read values
    # validate values


if __name__ == "__main__":
    app.run()

### SQlite-Server connection ###
Database = "airline_database.db"
conn = sqlite3.connect(Database)

# add data from form


