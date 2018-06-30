import json
import a001_mainScript as a001
import t001_mainScript as t001

races = int('3')
lanes = int('2')
country = 'DK'

number = 8

echoback = a001.raceProblem(races, lanes, country)
# echoback = t001.enterNumber(number)
print(echoback)
# returnString = json.dumps(echoback)