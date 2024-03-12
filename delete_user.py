from flask import flask

@app.route('/users/<name>', methods=['DELETE'])
def deleteUser(name):
    