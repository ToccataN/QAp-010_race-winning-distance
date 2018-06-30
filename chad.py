def buildEchoback(assumptionText, questionText, answerVal, instructionText):

    echoback = {
        'information' : assumptionText,
        'question' : questionText,
        'instruction' : instructionText,
        'answer' : answerVal,
    }

    return echoback