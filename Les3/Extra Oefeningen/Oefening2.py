# Vanuit een appartementsgebouw moet een politieagent het aantal betogers
# proberen te tellen.
# Maak hiervoor het volgende programma als hulpmiddel:
# • als de agent op Enter drukt, dan wordt 1 betoger bijgeteld.
# • als de agent op 1, 2 , ..., 9 drukt, dan wordt het opgegeven aantal bijgeteld.
# • als de agent S ingeeft, dan betekent dit dat hij wil stoppen. Hij krijgt dan wel nog eerst de
# vraag of hij echt wil stoppen J/N? Als het antwoord N of n is, ga dan weer verder met tellen.
# Als het antwoord J of j is, dan wordt het aantal getelde betogers afgedrukt.

stakers = 0
stoppen = ''
ingave = input("Druk op Enter voor elke nieuwe staker die je ziet.\nGeef een getal en dan Enter als je ineens een groepje wil doorgeven.\nDruk S en Enter als je wil stoppen.\n")

while stoppen != "J":
    tellen = input()
    if tellen == '':
        stakers +=1
    if tellen.isnumeric():
        stakers += int(tellen)
    if tellen == "S":
        stoppen = input("Wil je stoppen (J/N)? ").upper()


print("Totaal aantal stakers", stakers)