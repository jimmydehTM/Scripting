# De reeks van Fibonacci werd rond 1200 door Leonardo van Pisa voor het eerst beschreven.
# Deze rij wordt wiskundig als volgt beschreven: fn = f(n−1) + f(n−2) met n > 1.
# Deze rij start met de waarden 0 en 1. Elk volgend getal is de som van de 2 vorige getallen in de reeks
# Het resultaat wordt hieronder weergegeven:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# Schrijf een programma dat de reeks uitrekent zolang het resultaat kleiner is dan een door de
# gebruiker aangegeven grens.

getal = int(input("Tot welk getal wil je de reeks van Fibonacci drukken? "))

a = 0
b = 1
teller = 0
fib = 0

while fib < getal:
    print(a)
    fib = a + b
    a = b
    b = fib
    teller += 1