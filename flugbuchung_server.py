from flask import Flask, render_template, request
# import sqlite3

app = Flask(__name__)

### Localhost for HTML ###
@app.route("/startSite")
def start_site():
    return render_template("start_site_1.html")
    # add server-db interaction code


@app.route('/startSite', methods = ['POST', 'GET'])
def departairport():
    if request.method == 'GET':
        depart_airport = request.form["departAirport"]
        return render_template("choose_flight_2.html", depart_airport=depart_airport)


@app.route('/startSite', methods = ['POST', 'GET'])
def returnairport():
    if request.method == 'GET':
        return_airport = request.form["returnAirport"]
        return render_template("choose_flight_2-html", return_airport=return_airport)


@app.route('/startSite', methods = ['POST', 'GET'])
def departdate():
    if request.method == 'GET':
        depart_date = request.form["departDate"]
        return render_template("choose_flight_2.html", depart_date=depart_date)


@app.route('/startSite', methods=['POST', 'GET'])
def returndate():
    if request.method == 'GET':
        return_date = request.form["returnDate"]
        return render_template("choose_flight_2.html", return_date=return_date)


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


if __name__ == "__main__":
    app.run()

### SQlite-Server connection ###
# conn = sqlite3.connect()

