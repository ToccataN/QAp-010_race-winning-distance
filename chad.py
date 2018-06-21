def buildEchoback(assumptionText, questionText, answerVal):

    instructionText = "Assume that each person a) runs at a constant speed in all races, no matter the distance, and b) maintains this same speed start to finish in each race.  Round your answer to the nearest meter -- you're probably going to want to use a calculator."

    echoback = {
        'information' : assumptionText,
        'question' : questionText,
        'instruction' : instructionText,
        'answer' : answerVal,
    }

    return echoback