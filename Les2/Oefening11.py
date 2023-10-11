# De scouts verdelen hun leden in groepen die zij ‘takken’ noemen. Op basis van de leeftijd worden de
# scouts ingedeeld in 4 groepen.
# • Scouts jonger dan 12 zijn de Welpen.
# • Scouts van 12 tot en met 14 zijn de Jongverkenners.
# • Scouts van 15 tot en met 17 zijn de Verkenners.
# • Scouts vanaf 18 worden ingedeeld bij de Jins.
# Je gaat er in deze oefening vanuit dat kinderen onder de 8 jaar de toepassing niet gebruiken. Je hoeft
# hier dan ook geen extra controles voor te voorzien.
# Maak een programma dat vraagt naar je leeftijd en op basis daarvan de Scoutstak bepaalt.

leeftijd = int(input("Geef je leeftijd: "))

if leeftijd > 17:
    print("Je wordt ingedeelt bij de Jins")
elif leeftijd >= 15 and leeftijd < 18:
    print("Je wordt ingedeelt bij de Verkenners")
elif leeftijd >= 12 and leeftijd < 15:
    print("Je wordt ingedeelt bij de Jongverkenners")
else:
    print("Je wordt ingedeelt bij de Welpen")