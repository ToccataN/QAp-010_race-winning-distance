import chad

def enterNumber(number):

    informationText = ["This is a simple test API for set-up."]
    questionText = "Type " + str(number) + " into the box below."
    instructionText = "This is not a trick question"
    answer = (number, 'int')

    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack
