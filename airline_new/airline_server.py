#!/usr/bin/env python

# import libraries
from flask import Flask, render_template, request, Response
from datetime import date
import sqlite3

# start server
app = Flask(__name__)

# establish database connection
DATABASE = 'airline_database_new.db'


# functions
def create_running_number(attribute, relation):
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(f"SELECT MAX({attribute}) FROM {relation};")
    try:
        number = str(cur.fetchone()[0] + 1)
    except:
        number = 0
    con.close()
    return number


# home
@app.route('/')
def home():
    return render_template("home.html")


# display data and destination form
@app.route('/search_flight')
def search_flight():
    return render_template("search_flight.html")


# display flight choices form (choose 1)
@app.route('/get_flight', methods=['POST'])
def get_flight():
    try:
        departureAirport = request.values.get('departureAirport')
        targetAirport = request.values.get('targetAirport')
        flightDate = request.values.get('flightDate')
        passengerNumber = request.values.get('passengerNumber')

        con = sqlite3.connect(DATABASE)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM Flight "
                    "WHERE DepartureAirport LIKE ? AND TargetAirport LIKE ? AND DATE = ? AND FreeSeats >= ?",
                    (departureAirport, targetAirport, flightDate, passengerNumber))
        flights = cur.fetchall()

        response = app.make_response(render_template('get_flight.html',
                                                     flights=flights,
                                                     departureAirport=departureAirport,
                                                     targetAirport=targetAirport,
                                                     flightDate=flightDate,
                                                     passengerNumber=passengerNumber))
        response.set_cookie('flightDate', flightDate)
        response.set_cookie('passengerNumber', passengerNumber)

    except Exception as e:
        con.rollback()
        msg = "error: " + e
        print(msg)

    finally:
        con.close()
        return response


# display passenger data form and chosen flight
@app.route('/passenger_data', methods=['POST', 'GET'])
def passenger_data():
    if request.method == 'POST':
        flightNumber = request.form['FlightNumber']

    # save flight number as cookie
    response = app.make_response(render_template('passenger_data.html', flightNumber=flightNumber))
    response.set_cookie('flightNumber', flightNumber)

    return response


# save passenger data
@app.route('/confirm_data', methods=['POST', 'GET'])
def confirm_data():
    if request.method == 'POST':
        # works
        firstName = request.values.get('firstName')
        lastName = request.values.get('lastName')
        address = request.values.get('address')
        postCode = request.values.get('postCode')
        location = request.values.get('location')
        mailAddress = request.values.get('mailAddress')
        phoneNumber = request.values.get('phoneNumber')
        prefix = request.values.get('prefix')
        flightNumber = request.cookies.get('flightNumber')
        SSN = create_running_number('SSN', 'Person')

        con = sqlite3.connect(DATABASE)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM Flight WHERE FlightNumber = ?", (flightNumber, ))
        flight = cur.fetchone()

        response = app.make_response(render_template('confirm_data.html',
                                                     firstName=firstName,
                                                     lastName=lastName,
                                                     address=address,
                                                     postCode=postCode,
                                                     location=location,
                                                     mailAddress=mailAddress,
                                                     prefix=prefix,
                                                     phoneNumber=phoneNumber,
                                                     flight=flight))
        # save passenger data in cookie
        response.set_cookie('firstName', firstName)
        response.set_cookie('lastName', lastName)
        response.set_cookie('address', address)
        response.set_cookie('postCode', postCode)
        response.set_cookie('location', location)
        response.set_cookie('mailAddress', mailAddress)
        response.set_cookie('phoneNumber', phoneNumber)
        response.set_cookie('SSN', SSN)
    con.close()
    return response


# enter passenger data to database
@app.route('/book_flight', methods=['POST', 'GET'])
def book_flight():
    if request.method == 'POST':
        try:
            # flight data
            flightNumber = request.cookies.get('flightNumber')
            flightDate = request.cookies.get('flightDate')
            passengerNumber = int(request.cookies.get('passengerNumber'))

            # person data
            SSN = request.cookies.get('SSN')
            firstName = request.cookies.get('firstName')
            lastName = request.cookies.get('lastName')
            address = request.cookies.get('address')
            postCode = request.cookies.get('postCode')
            location = request.cookies.get('location')

            # phone number
            phoneNumber = request.cookies.get('phoneNumber')


            #passenger and booking data
            passengerID = create_running_number('PassengerID', 'Passenger')
            bookingNumber = create_running_number('BookingNumber', 'books')
            mailAddress = request.cookies.get('mailAddress')
            bookingDate = date.today()
            seatClass = 3

            with sqlite3.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Person VALUES (?, ?, ?, ?, ?, ?);",
                            (SSN, firstName, lastName, address, postCode, location))

                cur.execute("INSERT INTO Passenger VALUES (?, ?)",
                            (SSN, passengerID))

                cur.execute("INSERT INTO has_phoneNumber VALUES (?, ?)",
                            (SSN, phoneNumber))

                cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (passengerID, flightNumber, flightDate, bookingDate, seatClass, bookingNumber, mailAddress))

                cur.execute("SELECT FreeSeats FROM Flight WHERE FlightNumber == ? AND Date == ?",
                            (flightNumber, flightDate))
                freeSeats = str(cur.fetchone()[0] - passengerNumber)

                cur.execute("UPDATE Flight SET FreeSeats == ? WHERE FlightNumber == ? AND Date == ?",
                            (freeSeats, flightNumber, flightDate))

                con.commit()

                msg = "Booking successfull!"

        except Exception as e:
            con.rollback()

            msg = "Error! Booking cancelled! " + e

        finally:
            con.close()
            return render_template("book_flight.html", msg=msg)


if __name__ == "__main__":
    app.run()
