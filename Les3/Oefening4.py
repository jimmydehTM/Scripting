# Schrijf een programma waarmee een gebruiker ‘Hoger Lager’ kan spelen. De computer neemt een
# getal dat de speler moet raden. Het programma gaat door tot de speler het getal geraden heeft en
# drukt dan ook af hoeveel beurten de speler nodig had om (met tips als Hoger of Lager) tot het
# resultaat te komen.

from random import randint

value = randint(0, 20)
aantal = 0
getal = int(input("Geef een positief getal tussen 0 en 20: "))

while getal != value:
    aantal += 1
    if getal > value:
        print("LAGER!")
    if getal < value:
        print("HOGER!")
    getal = int(input("Geef een positief getal: "))

print("Je hebt het getal geraden in", aantal, "beurten.")