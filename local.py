import json
import a001_main as a001
import f001_main as f001
import t001_main as t001

races = int('3')
lanes = int('2')
country = 'DK'

number = 8

# echoBack = a001.raceProblem(races, lanes, country)
# echoBack = t001.enterNumber(number)
echoBack = f001.priceAnnuity(country)

print(echoBack)
# returnString = json.dumps(echoBack)