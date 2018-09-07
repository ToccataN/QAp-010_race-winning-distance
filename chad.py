def buildEchoback(assumptionText, questionText, answer, instructionText):

    echoback = {
        'information' : assumptionText,
        'question' : questionText,
        'instruction' : instructionText,
        'answer' : answer,
    }

    return echoback