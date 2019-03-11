from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

### Localhost for HTML ###
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

### MySQL-Server connection ###
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

connection = mysql.connect()
cursor = connection.cursor()

