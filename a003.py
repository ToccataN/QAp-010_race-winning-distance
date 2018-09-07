import chad
from random import randint
from random import shuffle
from random import choice

def twoModesDistance():

    upperRate = 50
    upperTime = 30
    
    animal = choice(['man', 'woman', 'frog', 'elephant'])
    distUnit = choice(['miles', 'meters', 'feet'])
    timeUnit = choice(['second', 'minute', 'hour'])
    rateUnit = distanceUnit + " per " + timeUnit

    modeList = ['on foot', 'with a bicycle', 'in a stage coach', 'with a bicycle', 'in a stage coach', 'on a battleship', 'strapped to a cruise missile']
    shuffle(modeList)
    modeAlabel = modeList[0]
    modeBlabel = modeList[1]
    
    # Set-up set of internally consistent values for each rate, time, and distance
    rateA = randint(3, upperRate)
    timeA = randint(3, round(upperRate * upperTime / rateA))
    distA = rateA * timeA
    modeAList = [modeAlabel, (rateA, rateUnit), (timeA, timeUnit), (distA, distUnit)]

    rateB = randint(3, upperRate)
    timeB = randint(3, round(upperRate * upperTime / rateB))
    distB = rateB * timeB
    modeBList = [modeBlabel, (rateB, rateUnit), (timeB, timeUnit), (distB, distUnit)]

    timeTot = timeA + TimeB
    distTot = distA + distB
    
    # Will leave this here for now, as might be a variant to ask, but a float, and a bit awkward for now
    rateTot = distTot / TimeTot
    totList = ['total', (rateTot, rateUnit), (timeTot, timeUnit), (distTot, distUnit)]

    # Pick the mode (or total) from which we will provide two of the three parameters
    twoNumMode = randint(0, 2)

    # Two parameters from total, 1 each from modeA and modeB
    if twoNumMode == 0:
        # As/if need two parameters from total, then best (for now) not to bring total rate into it (which is a float)
        # Therefore hardwired to provide time and distance only
        twoParam = [totList[2], totList[3]]
        
        sing1Param = choice(modeAList[1:])
        sing2Param = choice(modeBList[1:])
    
    # Two parameters from modeA, 1 each from total and modeB
    elif twoNumMode == 1:
        pass

    # Two parameters from modeB, 1 each from total and modeA
    elif twoNumMode == 2:
        pass


    totalDistance = 82
    totalTime = 23
    
    
    
    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)


    return echoBack
