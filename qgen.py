# Using request to load in parsing option on GET command
from flask import Flask, request
from flask_cors import CORS, cross_origin

import a001, a002, a003, a004, a005, a006
import f001
import t001
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

    if pid == 't001':
        number = int(request.args.get('number'))
        if number is None:
            number = '999'
        apiReturn = t001.enterNumber(number)
   
    elif pid == 'a001':
        races = int(request.args.get('races'))
        lanes = int(request.args.get('lanes'))
        country = request.args.get('country')

        if races is None: races = 4
        if lanes != 2: lanes = 2
        if country is None: country = 'DK'
        apiReturn = a001.raceProblem(races, lanes, country)

    elif pid == 'a002':
        apiReturn = a002.fraction()      

    elif pid == 'a003':
        apiReturn = a003.twoModesDistanceSimple()

    elif pid == 'a004':
        apiReturn = a004.twoModesDistanceSimEq()

    elif pid == 'a005':
        apiReturn = a005.findNumber()

    elif pid == 'a006':
        numberPeople = int(request.args.get('people'))
        if numberPeople is None: numberPeople = 4
        apiReturn = a006.ratioProblem(numberPeople)

    elif pid == 'f001':
        country = request.args.get('country')
        apiReturn = f001.priceAnnuity(country)

    returnString = json.dumps(apiReturn)
    return returnString

if __name__ == '__main__':
    app.run(debug = True, use_reloader=True)