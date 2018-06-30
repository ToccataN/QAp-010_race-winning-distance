# Using request to load in parsing option on GET command
from flask import Flask, request
from flask_cors import CORS, cross_origin

import a001_mainScript as a001
import t001_mainScript as t001
import json

app = Flask(__name__)
CORS(app)

# Defined endpoint at /getq002

@app.route('/')

def get_question():

    # Determine which problem is being called
    pid = request.args.get('pid')
    if pid is None:
        pid = 't001'

    if pid == 'a001':
        races = int(request.args.get('races'))
        lanes = int(request.args.get('lanes'))
        country = request.args.get('country')

        if races is None: races = 4
        if lanes != 2: lanes = 2
        if country is None: country = 'DK'
        apiReturn = a001.raceProblem(races, lanes, country)

    if pid == 't001':
        number = int(request.args.get('number'))
        apiReturn = t001.enterNumber(number)
        
    returnString = json.dumps(apiReturn)
    return returnString

if __name__ == '__main__':
    app.run(debug = True, use_reloader=True)