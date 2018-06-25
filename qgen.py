# Using request to load in parsing option on GET command
from flask import Flask, request
from flask_cors import CORS, cross_origin

import F1_mainScript as mainScript
# import datetime
import json

app = Flask(__name__)
CORS(app)

# Defined endpoint at /getq002

@app.route('/')

def get_question():

    # Set number of runners
    numberOfracers = 4

       echoback = mainScript.raceProblem(numberOfracers)


    returnString = json.dumps(echoback)

    print(returnString)

    return returnString

if __name__ == '__main__':
    app.run(debug = True, use_reloader=True)
