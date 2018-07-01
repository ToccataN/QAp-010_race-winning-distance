import chad

# [Your cousin Olga]  in [Skarsgard] has received an offer to purchase an annity. It promises to pay  [120] [kroner] on each annual anniverary of the purchase date for [20] years.

# She has separately  determined that the risk rate on this annuity varies over time. For the first  year, she believes the discount rate that should be applied is [8.00%] p.a.  This rate increases by [20] bps [0.20%] p.a. each year afterwards. (To be  clear, this means that the discount rate for the final year of the annuity is  [xx.x]% p.a.)

# What is the maximum  price she should offer to pay for this annuity?

def priceAnnuity(country):

    informationText = ["This is a simple test API for set-up."]
    questionText = "Type " + country + " into the box below."
    instructionText = "This is not a trick question"

    echoBack = chad.buildEchoback(informationText, questionText, 99, instructionText)

    return echoBack
