import chad
from random import randint
from random import shuffle
from random import choice

def twoPeople():

    people = ['mother', 'daughter']
    badAges = True
    while badAges == True:

        badAges = False
        daughter = randint(5, 30)
        ratioNum = randint(3, 15)
        ratioDen = randint(1, 5)

        ratioVal = ratioNum / ratioDen
        mother = ratioVal * daughter
        totalAges = daughter + mother
        average = totalAges / 2
        deltaAge = mother - daughter
        # Just to ensure we have appropriate set-up
        if daughter % ratioDen != 0: badAges = True
        if deltaAge < 20 or deltaAge > 50: badAges = True
        if mother > 95: badAges = True
        if totalAges % 2 != 0: badAges = True
        
        print(mother, daughter, " badAges = ", badAges)

    ratString = str(ratioNum) + ":" + str(ratioDen)
    ages = [int(mother), daughter]
    answerPick = randint(0, 1)

    answer = ( ages[answerPick], 'int')

    informationText = []
    informationText.append("The average ages of a mother and her daughter is " + str(int(average)) + ".  The ratio of their ages is " + ratString + ".")
    
    questionText = "What is the " + people[answerPick] + "'s age?"
    instructionText = "Enter your answer in the box provided."
    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack