s = "qwertyforstytysixabcdefghthisisthecaseifwehavenoideas"

prevLetter = s[0]
seqBuilding = prevLetter
seqLength = 0

for letter in s[1:]:
    
    if letter >= prevLetter:
        seqBuilding += letter
        
    else:
        
        if len(seqBuilding) > seqLength:
            saveSequence = seqBuilding
            seqLength = len(saveSequence)
        
        seqBuilding = letter

    prevLetter = letter

# Clunky final test in the event longest sequence is at end of string (and loop ends naturally)
if len(seqBuilding) > seqLength:
    saveSequence = seqBuilding

print("Longest first-occurring substring is: ", saveSequence)