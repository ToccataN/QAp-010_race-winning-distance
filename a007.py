import chad
from random import randint

def twoPeople():

    people = ['Lars', 'Billy Jo']
    badAges = True
    while badAges == True:

        badAges = False
        second = randint(5, 80)
        ratioNum = randint(3, 21)
        ratioDen = randint(1, 12)

        ratioVal = ratioNum / ratioDen
        first = ratioVal * second
        totalAges = first + second
        average = totalAges / 2
        
        # Just to ensure we have appropriate set-up
        if first == second: badAges = True
        if first % ratioDen != 0: badAges = True
        if max(first, second) > 95: badAges = True
        if totalAges % 2 != 0: badAges = True
        
        print(first, second, " badAges = ", badAges)

    ratString = str(ratioNum) + ":" + str(ratioDen)
    ages = [int(first), second]
    answerPick = randint(0, 1)

    answer = ( ages[answerPick], 'int')

    informationText = []
    info0a = "The average age of " + people[0] + " and " + people[1] + " is " + str(int(average)) + ".  "
    info0b = "The ratio of their ages (" + people[0] + " : " + people[1] + ") is " + ratString + "."
    info = info0a + info0b
    informationText.append(info)
    
    questionText = "What is " + people[answerPick] + "'s age?"
    instructionText = "Enter your answer in the box provided."
    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack

def motherDaughter():

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