#!/usr/bin/python3
from pitstop import app
from flask import jsonify

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'Status': 'Ok'}), 200