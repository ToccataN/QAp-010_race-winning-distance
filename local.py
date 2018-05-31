import json
import F1_mainScript as mainScript

# subject, sou, and difficulty are search string arguments set-up for API
numberOfracers = 4

echoback = mainScript.raceProblem(numberOfracers)
print(echoback)
# returnString = json.dumps(echoback)