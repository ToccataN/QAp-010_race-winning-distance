def buildEchoback(assumptionText, questionText, answerVal):

    instructionText = "(Assume that each person runs at a constant speed in all races, no matter their distance, and their running speed does not vary across the races they run.)"

    echoback = {
        'information' : assumptionText,
        'question' : questionText,
        'instruction' : instructionText,
        'answer' : answerVal,
    }

    return echoback