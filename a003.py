import chad
from random import randint
from random import shuffle
from random import choice

# Decided to limit this version to very easy 'fill in the blank' in matrix, not example with two equations and two unknowns
# which I've now set-up in a004
def twoModesDistanceSimple():

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

    # The concept is that we need to specify (any) four independent variables from the 'matrix' that's available, from each of 'modes' A/B/Total
    # and "parameters": rate, time, and distance (where we tend to exclude using "total rate", given this is a blended average, and hence likely a non-integer
    # The four selected assumptions need to be 'distributed' such that two (2) are from one mode, and the remaining two are one each from the remaining modes
    # As well, we don't want any 3 of the 4 chosen parameters to be on the same dimensions, as this is redundant.
    # and then assumptions provided will be insufficient to answer the question.
    # So this is what brings in the checkThree function on the randomly selecting dimensionList and re-loops until set of 4 dimensions is valid

    validPick = False
    while validPick == False:
        
        # We start by picking the mode (including possibly 'total') from which we will provide two of the three parameters
        # twoParamMode = randint(0, 2)
        twoParamMode = 0

        # Then we figure out the mode from which we will select a parameter for the "answer", i.e. the question
        # We do this by ensuring that we don't pick the answer/question from the mode that we also assigned for two-parameters within assumptions (as that would be 'dumb')
        ansModeChoices = [0, 1, 2]
        ansModeChoices.remove(twoParamMode)
        ansParamMode = choice(ansModeChoices)

        # Two parameters from total, 1 each from modeA and modeB, which means that ansParamModel must be 1 or 2    

        if twoParamMode == 0:
            # As/if need two parameters from total, then best (for now) not to bring total rate into it (which is a float)
            # Therefore hardwired to provide time and distance only
            twoParam = [totList[1], totList[2]]
            
            # And pick any single one of rate, time, or distance tuple from modeA and modeB
            sing1Param = choice(modeAList)
            sing2Param = choice(modeBList)
    
            # Then we need to randomly select the answer parameter (from which we will frame question) from one of four parameters
            # remaining within either of the 'single parameter' modes
            if ansParamMode == 1:
                ansChoices = modeAList[:]
                ansChoices.remove(sing1Param)
            
            else:
                ansChoices = modeBList[:]
                ansChoices.remove(sing2Param)

        # Two parameters from modeA, 1 each from total and modeB, hence ansParamMode 0 or 2
        elif twoParamMode == 1:
            # Pick first two 2tuples from suffled list, which excludes label
            tupleList = modeAList[:]
            shuffle(tupleList)
            twoParam = tupleList[:2]
        
            sing1Param = choice(totList[1:])
            sing2Param = choice(modeBList)
            if ansParamMode == 0:
                ansChoices = totList[1:]
                ansChoices.remove(sing1Param)
            else:
                ansChoices = modeBList[:]
                ansChoices.remove(sing2Param)
        
        # Two parameters from modeB, 1 each from total and modeA
        elif twoParamMode == 2:
            tupleList = modeBList[:]
            shuffle(tupleList)
            twoParam = tupleList[:2]
        
            sing1Param = choice(totList[1:])
            sing2Param = choice(modeAList)
            if ansParamMode == 0:
                ansChoices = totList[1:]
                ansChoices.remove(sing1Param)
            else:
                ansChoices = modeAList[:]
                ansChoices.remove(sing2Param)

        if len(ansChoices) == 0:
            pass
        else:
            ansParam = choice(ansChoices)

        givenParamDimList = [sing1Param[1], sing2Param[1], twoParam[0][1], twoParam[1][1]]
        print(givenParamDimList, "Answer: ", ansParam)

        validPick = not checkThree(givenParamDimList)
        
        # Also need to check that don't have a 'dumb' question by having answer on dimension where 2 values already given (and not a rate)
        ansDim = ansParam[1]
        if countString(ansDim, givenParamDimList) >= 2 and ansDim != 'rate':
            validPick = False

        # Also, we can't have the 'missing' dimensiono on the twoParam mode match the dimension chosen for each of sing1 and sing2 (unless rate)
        # But only test this if the current set up is otherwise OK, i.e. validPick == True
        if sing1Param[1] == sing2Param[2] and sing1Param != 'rate' and validPick:
            dimList = ['rate', 'time', 'distance']
            dimList.remove(twoParam[0][1])
            dimList.remove(twoParam[1][1])
            missingDim = dimList[0]
            if sing1Param[1] == missingDim:
                validPick = False

        # Prevent the relatively 'tricky' version that ensues when 'rate' picked for both sing1 and sing2
        if sing1Param[1] == sing2Param[2] == 'rate':
            validPick = False

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