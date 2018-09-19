import chad
from random import randint
from random import shuffle
from random import choice

def twoModesDistanceSimEq():

    # Set upper limits in random picks for rate and time integers
    upperRate = 50
    upperTime = 30
    
    animal = choice(['man', 'woman', 'frog', 'gopher', 'penguin', 'giraffe', 'panda', 'polar bear', 'meerkat', 'gorilla', 'lemur', 'zebra'])
    distUnit = choice(['mile', 'meter', 'yard', 'light-year', 'micron', 'kilometer', 'league', 'nautical mile'])
    timeUnit = choice(['second', 'minute', 'month', 'day', 'week', 'fortnight', 'hour'])
    
    rateUnit = distUnit + " per " + timeUnit
    distUnit = distUnit + 's'
    timeUnit = timeUnit + 's'

    # For mode, structure a bit different, as need to randomly select two that are different.
    # Could go with CHOICE from a popped list, but this seems just as reasonable, pick first two from shuffled list.
    modes = ['on foot', 'by dog sled', 'in a hot air balloon', 'on a hovercraft', 'on a jeepney', 'by horse', 'on a cable car', 'with a bicycle', 'in a stage coach', 'in a sedan chair', 'on a battleship', 'aboard a felucca', 'strapped to a cruise missile']
    shuffle(modes)
    modeAlabel = modes[0]
    modeBlabel = modes[1]
    
    # Set-up set of internally consistent values for each rate, time, and distance
    rateA = randint(3, upperRate)
    timeA = randint(4, round(upperRate * upperTime / rateA))
    distA = rateA * timeA
    modeAList = [(modeAlabel, 'rate', rateA, rateUnit, 'at'), (modeAlabel, 'time', timeA, timeUnit, 'for'), (modeAlabel, 'distance', distA, distUnit, 'for')]

    rateB = randint(2, upperRate)
    timeB = randint(5, round(upperRate * upperTime / rateB))
    distB = rateB * timeB
    modeBList = [(modeBlabel, 'rate', rateB, rateUnit, 'at'), (modeBlabel, 'time', timeB, timeUnit, 'for'), (modeBlabel, 'distance', distB, distUnit, 'for')]

    timeTot = timeA + timeB
    distTot = distA + distB
    
    # Will leave this here for now, as might be a variant to set-up, i.e. as for some weighted average rate of travel
    # However, for now, since this requires a float answer, and a bit more awkward for now.  Will leave with 'even' integers.
    rateTot = distTot / timeTot
    totList = [('an average', 'rate', rateTot, rateUnit, 'of'), ('in total', 'time', timeTot, timeUnit, 'for'), ('in total', 'distance', distTot, distUnit, 'for')]

    # For this (trickier) problem, it's decided to set-up with total time and distance and provide rates for modes A and B
    # From that position, any of four possible answers are selected from remaining unknown info in modes A and B
    
    sing1Param = modeAList[0]
    sing2Param = modeBList[0]
    twoParam = totList[1:]
    ansParam = choice([modeAList[1], modeAList[2], modeBList[1], modeBList[2]])

    info0 = "A " + animal + " travels partly " + modeAlabel + " and partly " + modeBlabel + ".  If the " + animal + " travels:"
    info1a = firstCapital(sing1Param[0]) + " " + sing1Param[4] + " " + str(sing1Param[2]) + " " + sing1Param[3] + ";"
    info1b = firstCapital(sing2Param[0]) + " " + sing2Param[4] + " " + str(sing2Param[2]) + " " + sing2Param[3] + "; and"
    
    info20 = firstCapital(twoParam[0][0])
    info21 = twoParam[0][4] + " " + str(twoParam[0][2]) + " " + twoParam[0][3]
    info22 = twoParam[1][4] + " " + str(twoParam[1][2]) + " " + twoParam[1][3]
    info2 = info20 + " " + info21 + " " + info22

    informationText = [info0, info1a, info1b, info2]

    questionText = "What is the " + ansParam[1] + " in " + ansParam[3] + " that the " + animal + " travelled " + ansParam[0] + "?"
    answer = (ansParam[2], 'int')
    instructionText = "Enter your answer in the box provided.  No units, just the number."
    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack

def firstCapital(myString):

    capitalString = myString[0].upper() + myString[1:]

    return capitalString

def checkThree(myList):

    uniqueList = []
    uniqueList.append(myList[0])

    for myString in myList[1:]:
        if myString not in uniqueList:
            uniqueList.append(myString)

    uniqueCount = len(uniqueList)
    atLeastThree = False
    if uniqueCount <= 2:
        atLeastThree = True

    return atLeastThree

def countString(myString, myList):

    count = 0
    for element in myList:
        if element == myString:
            count = count + 1

    return count
