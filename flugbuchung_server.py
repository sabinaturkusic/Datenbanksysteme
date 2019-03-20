from flask import Flask, render_template, request
# from utils import get_db
import sqlite3

app = Flask(__name__)

DATABASE = 'airline_database.db'


### Localhost for HTML ###
@app.route("/startSite")
def start_site():
    return render_template("start_site_1.html")
    # add server-db interaction code


@app.route('/choose_flight_2.html',methods = ['POST', 'GET'])
def departairport():
    if request.method == 'GET':
        depart_airport = request.form["departAirport"]
        return render_template("choose_flight_2", depart_airport=depart_airport)


@app.route('/choose_flight_2.html',methods = ['POST', 'GET'])
def returnairport():
    if request.method == 'GET':
        return_airport = request.form["returnAirport"]
        return render_template("choose_flight_2", return_airport=return_airport)


@app.route('/choose_flight_2.html',methods = ['POST', 'GET'])
def departdate():
    if request.method == 'GET':
        depart_date = request.form["departDate"]
        return render_template("choose_flight_2", depart_date=depart_date)


@app.route('/choose_flight_2.html', methods=['POST', 'GET'])
def returndate():
    if request.method == 'GET':
        return_date = request.form["returnDate"]
        return render_template("choose_flight_2", return_date=return_date)


@app.route("/chooseFlight")
def choose_flight():
    return render_template("choose_flight_2.html")


# add server-db interaction code
# read values
# validate values


@app.route("/passengers")
def passengers():
    return render_template("passengers_3.html")


# add server-db interaction code
# read values
# validate values


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation_4.html")


# add server-db interaction code
# read values
# validate values


### this is a test ###
conn = sqlite3.connect(DATABASE)
sql = sqlite3


# display html fom
@app.route("/test")
def retrieve_from_data():
    return render_template("add_to_db.html")


# add to database from html
@app.route('/addToDB', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            first_name = request.values.get('first name')
            last_name = request.values.get('last name')
            address = request.values.get('address')
            postcode = request.values.get('post code', type=int)
            location = request.values.get('location')

            con = sqlite3.connect(DATABASE)
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT MAX(SSN) FROM Person;")
            SSN = cur.fetchone()[0] + 1
            con.close()

            with sql.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Person VALUES (?, ?, ?, ?, ?, ?);",
                            (SSN, first_name, last_name, address, postcode, location))
                con.commit()
                msg = "Record successfully added"

        except Exception as e:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()

# Zeigt alle Einträge zu person an
@app.route('/list')
def list():
    con = sql.connect(DATABASE)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Person")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


# @app.route('/')
# def retrieve_from_data():
#     return render_template("home.html")

### test end ###

if __name__ == "__main__":
    app.run()

### SQlite-Server connection ###
cursor = get_db().cusor()