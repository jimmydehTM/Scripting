# Schrijf een programma dat een eindcijfer inleest en vervolgens 10 getallen. Als antwoord krijg je het
# aantal getallen dat eindigt op het eindcijfer.
# Zorg ervoor dat de tekst wijzigt wanneer er slechts 1 getal eindigt op het eindcijfer.

aantal = 0

cijfer = int(input("Op welk eindcijfer wil je de getallen controleren? "))

for i in range(10):
    
    getal = int(input("Geef een getal: "))
    
    if getal % 10 == cijfer:
        aantal += 1
        

print(aantal, "van de 10 getallen eindigd op", cijfer)