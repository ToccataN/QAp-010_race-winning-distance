import json
import a001_mainScript as a001

races = 3
lanes = 2
country = 'DK'

echoback = a001.raceProblem(races, lanes, country)
print(echoback)
# returnString = json.dumps(echoback)