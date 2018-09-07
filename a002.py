import chad
from random import randint

def fraction():

    minDelta = -12
    multiple = randint(3, 20)
    numPrime = randint(2, 10)
    denPrime = multiple * numPrime

    # Sets lower bound on random pick to ensure numerator not negative
    upperNumdelta = numPrime - 1
    deltaNum = randint(minDelta, upperNumdelta)

    upperDendelta = denPrime - 1
    deltaDen = randint(minDelta, upperDendelta)

    denom = denPrime - deltaDen
    numer = numPrime - deltaNum
    delta = denom - numer
    
    answerVal = str(numer) + "/" + str(denom)
    answer = (answerVal, 'str')
    
    deltaChangeWord = changeWord(delta, ("less", "more"))
    numChangeWord = changeWord(deltaNum, ("increased", "decreased"))
    denChangeWord = changeWord(deltaDen, ("increased", "decreased"))

    info1 = "The numerator of a fraction is " + str(abs(delta)) + " " + deltaChangeWord + " than its denominator."

    info2a = "If the numerator is " + numChangeWord + " by " + str(abs(deltaNum))
    info2b = " and the denominator is " + denChangeWord + " by " + str(abs(deltaDen)) + ", "
    info3 = "then the denominator becomes " + str(multiple) + " times the numerator."
    info = info1 + "  " + info2a + info2b + info3

    informationText = []
    informationText.append(info)

    questionText = "What is the fraction?"
    instructionText = "Enter your answer in format separated by / character, i.e. numer / denom."

    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack

def changeWord(number, textTuple):

    if number > 0:
        returnString = textTuple[0]
    else:
        returnString = textTuple[1]
    
    return returnString