# Adding a User
from flask import Flask


@app.route('/users/', methods=['POST'])
def add():
    name = request.form['nm']
    phone_number = request.form['pn']
    return name, phone_number

if __name__ == "__main__":
    app.run(debug = True)
