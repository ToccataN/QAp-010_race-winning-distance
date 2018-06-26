import itertools
import random
import timeit
import numpy as np

import chad

def raceProblem(races, lanes, country):

#    namesList = ['Andrew', 'Brittany', 'Carson', 'Derlene', 'Edward', 'Fritz']
    namesList = ['Astrid', 'Christian', 'Freya', 'Ingeborg', 'Mads', 'Poul']

# Danish girls: Trine, Astrid, Rikke, Silja, Ingeborg, Alberte, Luna, Freya, Mathilde, Signe, Amalie, Milla, Ella
# Danish boys: Frederik, Rasmus, Magnus, Ulrich, Andreas, Asger, Bertram, Poul, Henrik, Niklas, Gustav, Mads, Christian, Mikkel, Nicolai, Emil, Thanush, Sigurd, Witsel, Thaifred



    # Maximum of six names
    # Logic of problem presumes runners always run same speed in each race
    # Logic works currently for pairings only (lanes = 2)
    # Since each runner runs twice (including final race), and there are two lanes, this means total races, including final, is also = numberOfracers
    # "Heats" refers to the races in which results already in, referred to as "preliminary races" in the question text.
    # Final race is the race for which winning distance is formed as question

    # racesCount = 2 * numberOfracers / lanes # DUBIOUS!!, but generally is how things (roughly) would work, presuming structure of assumptions is such that returns integer.
    # races = int(raceCount)
    
    # Must be only 2-person races, i.e. lanes = 2, for now based on how the logic works for selecting winner of each race
    # lanes = 2
    numberOfracers = races                  # This works only when lanes = 2, as each racer needs to be in two races
    maxRaceDistance = 32                    # multiplied by 100 in actual meters

    racerNames = namesList[:numberOfracers] # deliberately set-up to provide alphabetical a, b, c names for time being
    print(racerNames)

    heatCount = races - 1

    # Set up nTuple of 'racer registration numbers', simple sequenced tuple of integers from 1 to number of racers
    racerNumlist = []
    for i in range(numberOfracers):
        racerNumlist.append(i + 1)
    racers = tuple(racerNumlist)
    print("Racers: ", racers)

    # Set random selection of who beats whom in the (prelim) heats.
    # speedOrder is set here for final race, but this is essentially ignored since the race order in the final race
    # must be derived by win distance parameters from heats, NOT by this combination.
    speedOrder = racerNumlist[:]
    random.shuffle(speedOrder)
    print("speedOrder:", speedOrder)

    # racePairs is the listing of 2tuples of who's racing, before consideration of who wins each race
    racePairs = []
    for i in range(numberOfracers - 1):
        raceTuple = (i + 1, i + 2)
        racePairs.append(raceTuple)

    # Last pair simply hard-wired as final racer and first racer paired up
    finalPair = (numberOfracers, 1)
    racePairs.append(finalPair)

    # Actual race pairs then determined from shuffle to provide some further variability between pairings in heats vs. final race
    random.shuffle(racePairs)
    print("racePairs: ", racePairs)

    # resultPairs is now the list that is sensitive to who should be winning (in the heats) based on speedOrder
    resultPairs = []
    for pair in racePairs:

        # Testing position in speedOrder sequence to determine adding tuples such that winner listed first when resultPairs constructed
        if speedOrder.index(pair[0]) < speedOrder.index(pair[1]):
            resultPair = pair
        else:
            resultPair = (pair[1], pair[0])

        resultPairs.append(resultPair)
        print("Race result pair: ", resultPair)

    raceDistances = []
    winDistances = []

    # This loop sets up random assumptions for problem generation
    # Note that a winning distance for final race is generated, since it 'comes along with' race distance, which we DO need for final race
    for i in range(races):
        currentRaceDistance = 100 * random.randint(1, maxRaceDistance)
        currentWinDistance = random.randint(1, round(currentRaceDistance / 4))
        raceDistances.append(currentRaceDistance)
        winDistances.append(currentWinDistance) # Note final win distance ignored, as this is the question, not an input
        print("Race ", i + 1, ":", resultPairs[i], " Distance = ", currentRaceDistance, " meters; Win margin = ", winDistances[i], " m" )

    # This block sets up the "lambda array" for final race, where 1 indicates the (presumed) winner and -1 the loser.
    # Racers not in final race show zero
    targetLambdas = [0] * numberOfracers
    finalPair = resultPairs[-1]
    targetLambdas[finalPair[0] - 1] = 1
    targetLambdas[finalPair[1] - 1] = -1
    print("TargetLambdas: ", targetLambdas)

    # This loop does a brute force check through all combinations of "flip multipliers" to determine which combination yields
    # the 'cancelling out' consistent with targetLambdas
    i = 0
    flipMultsIter = itertools.product((1, -1), repeat = heatCount)
    for flipMult in flipMultsIter:
        i = i + 1
        # print("flipMult No. ", i, ": ", flipMult)

        cumLambdas = [0] * numberOfracers
        runnerLambdas = np.zeros(( numberOfracers, heatCount))
        for racer in racerNumlist:

            heatNo = 0
            for heatResult in resultPairs[:-1]:
                heatNo = heatNo + 1
                if racer not in heatResult:
                    heatLam = 0
                else:
                    if racer == heatResult[0]:
                        heatLam = 1
                    else:
                        heatLam = -1

                runnerLambdas[racer - 1, heatNo - 1] = heatLam
                cumLambdas[racer - 1] = cumLambdas[racer - 1] + flipMult[heatNo - 1] * heatLam

        print("cumLambdas: ", cumLambdas, " for flipMult = ", flipMult)
        if cumLambdas == targetLambdas:
            flipAnswer = flipMult
            print("flipAnswer = ", flipAnswer)

    print("runnerLambdas: ", runnerLambdas)

    speedRats = []
    cumSpeedRatio = 1.0
    # cumSpeedRatio is an accumulated multiplication, where the "flipAnswer" value is used as an expondent to determine whether effectively multiplied or divided
    for i in range(heatCount):
        speedRatio = raceDistances[i] / (raceDistances[i] - winDistances[i])
        speedRats.append(speedRatio)
        cumSpeedRatio = cumSpeedRatio * speedRatio ** flipAnswer[i]

    print("cumSpeedRatio: ", cumSpeedRatio, " i.e. based on pre-ordered finishing of final pair")
    if cumSpeedRatio < 1:
        finalResultPair = (finalPair[1], finalPair[0])
        resultSpeedRatio = 1 / cumSpeedRatio
    else:
        finalResultPair = finalPair
        resultSpeedRatio = cumSpeedRatio

    finalWinDistance = raceDistances[numberOfracers - 1] * (resultSpeedRatio - 1) / resultSpeedRatio

    print(finalResultPair[0], " beats ", finalResultPair[1], " by ", finalWinDistance, " meters.  resultSpeedRatio = ", resultSpeedRatio)

    # Text generation of/for the text that sets the assumptions related to results from the 'heats'
    informationText = []
    informationText.append("You have the following results from preliminary races:")
    i = 0
    for pair in resultPairs[:-1]:
        winner = namesList[pair[0] - 1]
        loser = namesList[pair[1] - 1]
        statement = winner + " beats " + loser + " by " + str(winDistances[i]) + " meters in a " + str(raceDistances[i]) + "-meter race."
        # print(statement)
        informationText.append(statement)
        i = i + 1

    print(informationText)

    winner = namesList[finalResultPair[0] - 1]
    loser = namesList[finalResultPair[1] - 1]

    questionText = "By how many meters will " + winner + " beat " + loser + " in a " + str(raceDistances[races - 1]) + "-meter race?"
    print(questionText)

    finalWinDistance = round(finalWinDistance)
    answerText = "Answer: " + winner + " will win by " + str(round(finalWinDistance)) + " meters.  (Rounded to nearest meter)"
    print(answerText)

    echoBack = chad.buildEchoback(informationText, questionText, round(finalWinDistance))

    return echoBack
