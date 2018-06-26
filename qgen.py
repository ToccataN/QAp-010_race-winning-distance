# Using request to load in parsing option on GET command
from flask import Flask, request
from flask_cors import CORS, cross_origin

import a001_mainScript as a001
import json

app = Flask(__name__)
CORS(app)

# Defined endpoint at /getq002

@app.route('/')

def get_question():

    # Determine which problem is being called
    pid = request.args.get('pid')

    if pid == 'a001':
        races = int(request.args.get('races'))
        lanes = int(request.args.get('lanes'))
        country = request.args.get('country')
        echoback = a001.raceProblem(races, lanes, country)

    returnString = json.dumps(echoback)
    return returnString

if __name__ == '__main__':
    app.run(debug = True, use_reloader=True)
