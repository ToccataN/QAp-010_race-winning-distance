import chad
from random import randint
from random import shuffle
from random import choice

def ratioProblem():

    numberRenters = 4
    renterList = ['A', 'B', 'C', 'D', 'E', 'F']
    renterList = renterList[:numberRenters]

    keepLooping = True
    while keepLooping:

        rentDict, totalRent = setRents(renterList)
        print("Next rentList: ", rentDict, "totalRent = ", totalRent)
        keepLooping = isSameRent(rentDict)

    numberRatios = numberRenters - 1
    shuffle(renterList)

    # Build initial chain of ratios as list of 2tuples
    ratioList = []
    for index in range(numberRatios):

        flipRatio = randint(0, 1)
        if flipRatio == 1:
            ratioList.append((renterList[index + 1], renterList[index]))
        else:
            ratioList.append((renterList[index], renterList[index + 1]))

    print("ratioList:", ratioList)

    # Develop simplified ratios consistent with ratio list
    ratioValList = []
    for renterNum, renterDen in ratioList:
        rentRatio = simpString(rentDict[renterNum], rentDict[renterDen], ":")
        
        # print("rentRatio: ", rentRatio)
        ratioValList.append((renterNum, renterDen, rentRatio))
    
    # Construct list of each element of list as a fraction of total
    answerDict = {}
    for renter in renterList:
        answerDict[renter] = simpString(rentDict[renter], totalRent, "/")

    print("----------")
    print("ratioValList: ", ratioValList)
    print("Answers: ", answerDict)

    targetRenter = choice(renterList)
    answer = (answerDict[targetRenter], 'str')

    informationText = []
    informationText.append("A number of people are sharing rent, where you are given what they pay in a number of ratios:")
    for index in range(numberRatios):
        ratioLine = ratioValList[index][0] + "'s rent to " + ratioValList[index][1] + "'s is in the ratio " + ratioValList[index][2]
        informationText.append(ratioLine)
        
    questionText = "What is the fraction that represents " + targetRenter + "'s share of the total?"
    instructionText = "Enter your answer as a fraction, i.e. two numbers separated by the / character.  Ensure your fraction is entered in simplest form."
    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack

def setRents(renterList):

    # Idea here via choice function, is just to distort the probability of picking certain numbers
    primes = [2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 7, 7, 11]
    maxFactorCount = 4

    factorList = []
    # Loop one less than count, as reserve one space for a 'big prime'
    for i in range(maxFactorCount):
        factorList.append(choice(primes))

    rentDict = {}
    totalRent = 0
    for renter in renterList:
        factorCount = randint(1, maxFactorCount)
        shuffle(factorList)

        rentAmount = 1
        for i in range(0, factorCount - 1):
            rentAmount = rentAmount * factorList[i]
        
        rentDict[renter] = rentAmount
        totalRent = totalRent + rentAmount

    return (rentDict, totalRent)

def isSameRent(rentDict):

    amountList = []
    sameRent = False

    for renter, rentAmount in rentDict.items():
        if rentAmount in amountList:
            sameRent = True

        amountList.append(rentAmount)

    return sameRent

def gcd(a, b):
    
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)

def simpString(num, den, sep):

    GCDfactor = gcd(num, den)
        
    simpNum = int(num / GCDfactor)
    simpDen = int(den / GCDfactor)

    return str(simpNum) + sep + str(simpDen)