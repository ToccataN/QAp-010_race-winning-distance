def buildEchoback(assumptionText, questionText, answerVal):

    instructionText = "However fast each person may be, assume he/she runs at the same speed in all races, no matter the distance, and that his/her speed is constant from start to finish.  Round your answer to the nearest meter -- you're probably going to want to use a calculator."

    echoback = {
        'information' : assumptionText,
        'question' : questionText,
        'instruction' : instructionText,
        'answer' : answerVal,
    }

    return echoback