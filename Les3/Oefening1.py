# a) Met dit programma kan je het product van een aantal getallen berekenen. Het programma blijft
# aan de gebruiker gehele getallen vragen tot deze een 0 (nul) invoert. Wanneer de gebruiker 0
# ingeeft, wordt het product van de getallen afgedrukt

getal =  int(input("Geef een reeks getallen, stop door een 0 in te geven: "))
totaal = 0
aantal_getallen = 0

while getal != 0:
    aantal_getallen += 1
    totaal += getal
    getal =  int(input("Geef een reeks getallen, stop door een 0 in te geven: "))
    
print("Het product van de getallen is", totaal)
print("Het aantal getallen is", aantal_getallen)