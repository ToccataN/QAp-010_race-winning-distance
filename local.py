import json
import a001_mainScript as a001

races = int('3')
lanes = int('2')
country = 'DK'

echoback = a001.raceProblem(races, lanes, country)
print(echoback)
# returnString = json.dumps(echoback)