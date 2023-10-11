# Schrijf een programma om te bepalen of het jaartal dat je invoert een schrikkeljaar is of niet. Je
# programmeert zelf (zonder gebruik van Pythonfuncties) de volgende regels:
# • Voor de jaren voor 1582 geldt de regel dat als ze deelbaar zijn door 4 het jaar een schrikkeljaar is;
# • Na 1582 geldt de volgende regeling (enkel de voorwaarde die eerst staat, is van toepassing).
# • deelbaar door 4000: geen schrikkeljaar
# • deelbaar door 400: wel schrikkeljaar
# • deelbaar door 100: geen schrikkeljaar
# • deelbaar door 4: wel een schrikkeljaar
# Voorbeelden
# 1987 geen
# 2000 wel
# 1988 wel
# 1900 geen
# 1000 wel
# 8000 geen


invoer = int(input("Geef een jaartal: "))


if invoer < 1582 and (invoer % 4) == 0:
    print("Wel een schrikkeljaar!")
elif invoer > 1581 and invoer >= 4000 and invoer % 4000 == 0:
    print("Geen schrikkeljaar")
elif invoer > 1581 and invoer % 400 == 0:
    print("Wel een schrikkeljaar")
elif invoer > 1581 and invoer % 100 == 0:
    print("Geen schrikkeljaar")
elif invoer > 1581 and invoer % 4 == 0:
    print("Wel een schrikkeljaar")
else: print("Geen schrikkeljaar")