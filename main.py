import sqlite3
from flask import Flask

app = Flask(__name__)

try:
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
except sqlite3.Error as error:
    print(error)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/users/<name>', methods=['DELETE'])
def deleteUser(name):
    cursor.execute("DELETE FROM USERS WHERE NAME = " + name + ";")
    return 200

@app.route('/users/', methods=['POST'])
def add():
    name = request.form['nm']
    phone_number = request.form['pn']
    return name, phone_number
