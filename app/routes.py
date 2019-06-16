from app import app

from flask import Response, jsonify

from main import runServer, getLines

@app.route('/runserver')
def index():
    return runServer()

@app.route('/getstatus')
def status():
    return jsonify(getLines())

