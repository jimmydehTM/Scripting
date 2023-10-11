# Elektriciteitsmaatschappijen rekenen aan hun klanten jaarlijks een vast bedrag van 83.6 €
# (aansluiting, meterhuur, onderhoud, ...) aan. ’s Nachts betaal je per kWh 0,035 €. Overdag betaal je
# per kWh 0,068 €. Daar bovenop moet de klant ook 21% BTW betalen.
# Maak een programma dat berekent hoeveel je moet betalen. Eerst moet de gebruiker zijn gegevens
# ingeven. Het verbruik, in kWh (kilowatt per uur) is altijd een geheel getal.
# Daarna krijgt de klant een overzicht van zijn rekening.

vasteKost = 83.6
verbruikOverdag = int(input("Geef je verbruikt overdag (in kwh): "))
verbruikSnachts = int(input("Geef je verbruikt 's nachts (in kwh): "))

print("Factuur")
print("*******")
print("Vaste kosten: ",vasteKost)
print("Dagverbruik: ",verbruikOverdag*0.068)
print("Nachtverbruik: ",verbruikSnachts*0.035)
print("Totaal exclusief BTW: ",(verbruikOverdag*0.068) + (verbruikSnachts*0.035 + vasteKost))
print("Totaal inclusief BTW: ",((verbruikOverdag*0.068) + (verbruikSnachts*0.035 + vasteKost)) * 1.21)