import json
import a001_mainScript as a001
import t001_mainScript as t001

races = int('3')
lanes = int('2')
country = 'DK'

number = 8

# echoBack = a001.raceProblem(races, lanes, country)
echoBack = t001.enterNumber(number)
print(echoBack)
# returnString = json.dumps(echoBack)