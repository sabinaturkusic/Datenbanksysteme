from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)
connection = sqlite3.connect("test_database.db")


@app.route('/test1')
def new_student():
    return render_template('test1.html')

