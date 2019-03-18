from flask import Flask, render_template, request
# from utils import get_db
import sqlite3

app = Flask(__name__)


### Localhost for HTML ###
@app.route("/startSite")
def start_site():
    return render_template("start_site_1.html")
    # add server-db interaction code


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
conn = sqlite3.connect("airline_database.db")
sql = sqlite3


@app.route("/test")
def retrieve_from_data():
    return render_template("addrec.html")


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            SSN = request.form.get('SSN', type=int)
            first_name = request.values.get('first name')
            last_name = request.values.get('last name')
            address = request.values.get('address')
            postcode = request.values.get('post code', type=int)
            location = request.values.get('location')

            with sql.connect("airline_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Person VALUES (?, ?, ?, ?, ?, ?);",
                            (SSN, first_name, last_name, address, postcode, location))
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            print("in rollback" + str(e))
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("airline_database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Person")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


# @app.route('/home')
# def retrieve_from_data():
#     return render_template("home.html")

### test end ###

if __name__ == "__main__":
    app.run()

### SQlite-Server connection ###
Database = "airline_database.db"

cursor = get_db().cusor()
