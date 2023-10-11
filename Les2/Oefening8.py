# Schrijf een programma waarmee je kan beoordelen of het een stom, goed of fantastisch feestje is.
# Dit oordeel hangt af van het aantal flessen wijn en het aantal pizza’s dat de gebruiker inleest.
# - Het feestje is goed als er minstens 5 pizza’s en 5 flessen wijn zijn
# - Het feestje is fantastisch als daar bovenop het aantal pizza’s dubbel zo groot is als het aantal
# flessen wijn (of omgekeerd)
# - In alle andere gevallen is het een stom feestje.

wijn = int(input("Hoeveel flessen wijn zijn er: "))
pizza = int(input("Hoeveel pizza's is er: "))

if wijn < 5 or pizza < 5:
    print("Stom feestje")
elif (pizza == wijn *2) or (wijn == pizza * 2):
        print("Fantastisch feestje!")
else:
        print("Goed feestje")
