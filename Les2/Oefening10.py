# Iemands BMI (body mass index) wordt als volgt berekend: (gewicht/lengte**2)*10000

# De waarde van de BMI is bepalend om een oordeel uit te spreken over het gewicht van een
# (volwassen) persoon:
# • BMI < 18 ondergewicht
# • 18  BMI < 25 normaal gewicht
# • 25  BMI < 27 licht overgewicht
# • 27  BMI < 30 matig overgewicht
# • 30  BMI < 40 ernstig overgewicht
# • BMI  40 ziekelijk overgewicht
# Maak een programma dat vraagt naar je gewicht en je lengte en op basis daarvan het besluit toont.

gewicht = int(input("Geef je gewicht in kg: "))
lengte = int(input("Geef je lengte in centimeter: "))

bmi = (gewicht / (lengte**2))*10000

print("Een persoon van", gewicht, "kg met een lengte van", lengte, "cm heeft als BMI", bmi)
if bmi < 18:
    print("Dit is ondergewicht")
elif bmi == 18 or bmi < 25:
    print("Dit is normaal gewicht")
elif bmi == 25 or bmi < 27:
    print("Dit is licht overgewicht")
elif bmi == 27 or bmi < 30:
    print("Dit is matig overgewicht")
elif bmi == 30 or bmi < 40:
    print("Dit is ernstig overgewicht")
else:
    print("ziekelijk overgewicht")
