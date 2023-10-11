# Schrijf een programma waarmee je een trap kan
# laten tekenen. De gebruiker geeft alleen door
# hoeveel treden er moeten zijn.

aantal = int(input("Hoeveel treden heeft de trap: "))
a = "#####"
b = ""

for i in range(aantal):
    b = b + a
    print(b)
    print(b)
    