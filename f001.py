import chad
from random import randint

# She has separately  determined that the risk rate on this annuity varies over time. For the first  year, she believes the discount rate that should be applied is [8.00%] p.a.  This rate increases by [20] bps [0.20%] p.a. each year afterwards.

# What is the maximum  price she should offer to pay for this annuity?

def priceAnnuity(country):

    years = randint(10, 40)

    namesList = ['Astrid', 'Christian', 'Freya', 'Ingeborg', 'Mads', 'Poul']
    namePick = randint(1, len(namesList))
    person = namesList[namePick - 1]

    # Information first paragraph
    cityList = ['Copenhagen', 'Aarhus', 'Odense', 'Aalborg', 'Esbjerg', 'Randers', 'Kolding', 'Horsens', 'Vejle', 'Roskilde', 'Herning', 'Hørsholm']
    cityPick = randint(1, len(cityList))
    city = cityList[cityPick -1]

    amount = randint(100, 999)
    currency = 'krone'

    informationText1a = "Your cousin " + person + " in " + city + " has received an offer to purchase an annuity.  "
    informationText1b = "It promises to pay " + str(amount) + " " + currency + " on each annual anniversary of the purchase date for " + str(years) + " years."
    informationText1 = informationText1a + informationText1b
    
    # Information second paragraph
    initialDiscount = randint(100, 1000) / 100
    bpIncrease = randint(10, 99)

    informationText2a = person + " has separately  determined that the risk rate on this annuity varies over time.  "
    informationText2b = "For the first year, your cousin believes the discount rate that should be applied to the cash flows is " + str(initialDiscount) + "% p.a.  "
    informationText2c = "This rate increases by " + str(bpIncrease) + " bps (" + str(bpIncrease / 100) + "%) each year afterwards."  
    informationText2 = informationText2a + informationText2b + informationText2c

    # Form up information
    informationText = []
    informationText.append(informationText1)
    informationText.append(informationText2)

    questionText = "What is the maximum price your cousin should pay for this annuity?"
    instructionText = "Enter your answer, rounded to the nearest " + currency + " in the box provided"

    # Calculate answer
    pvFactor = 1.0
    discountRate = initialDiscount / 100
    price = 0
    for n in range(1, years + 1):
        
        pvFactor = pvFactor / (1 + discountRate)
        price = price + pvFactor * amount

        discountRate = discountRate + bpIncrease / 100 / 100
        print(n, discountRate, pvFactor, price)

    answer = (round(price), 'int')
    echoBack = chad.buildEchoback(informationText, questionText, answer, instructionText)

    return echoBack
