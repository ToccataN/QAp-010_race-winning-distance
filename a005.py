import chad
from random import randint
from random import choice

def findNumber():

    smallPrimes = [2, 2, 2, 3, 3, 5]
    bigPrimes = [7, 11, 13]
    factorCount = 5

    factorList = []
    # Loop one less than count, as reserve one space for a 'big prime'
    for i in range(factorCount - 1):
        factorList.append(choice(smallPrimes))
    factorList.append(choice(bigPrimes))

    numKfactors = randint(2, factorCount - 2)
    k = 1
    for i in range(0, numKfactors):
        k = k * factorList[i]

    dA = 1
    dAindices = range(0, factorCount)[numKfactors:]
    for i in dAindices:
        dA = dA * factorList[i]

    x = 1
    numXfactors = randint(2, factorCount - 2)
    xChoices = factorList[:]
    for i in range(numXfactors):
        nextFactor = choice(xChoices)
        # print("nextFactor = ", nextFactor)
        x = x * nextFactor
        xChoices.remove(nextFactor)

    r1 = randint(2, 5)
    nA = int(r1 + k * dA / x)

    r2 = randint(2, 6)
    dB = r2 * dA
    nB = r1 * r2

    mult = randint(3, 6)

    # print("Number of k factors = ", numKfactors)

    # print("factorList = ", factorList)
    # print("k = ", k)
    # print("dA =", dA)
    # print("x, numXfactors =", x, numXfactors)

    frac1 = str(nA) + "/" + str(dA)
    frac2 = str(nB) + "/" + str(dB)

    # equationString = str(nA) + "/" + str(dA) +"x = " + str(nB) + "/" + str(dB) + "x + " + str(k)
    # print(equationString)

    info1 = frac1 + " of a number exceeds "
    info2 = frac2 + " of the number by " + str(k) + "."
    informationText = []
    informationText.append(info1 + info2)

    questionText = "What is " + str(mult) + " times the number?"
    answer = (mult * x, 'int')
    instructionText = "Enter your answer in the box provided."
    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack