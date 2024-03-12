from flask import Flask
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()


phone_idx = 0

@app.route('/users/<name>', methods=['GET'])
def phone_number(name):
    res = cur.execute("SELECT phone_number FROM USERS WHERE name='"+name +"'")
    users = res.fetchone()  
    if len(users != 0):
        print(users)

