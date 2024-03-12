from flask import Flask

phone_idx = 0

@app.route('/users/<name>')
def phone_number(name):
    res = cur.execute("SELECT name FROM sqlite_master")
    users = res.fetchone()  
    if len(users != 0):
        print(users[phone_idx])

