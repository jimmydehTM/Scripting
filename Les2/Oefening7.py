getal_1 = int(input("Geef een getal: "))
getal_2 = int(input("Geef nog een getal: "))

if getal_1 == getal_2:
    print("Het antwoord voor de getallen", getal_1, "en", getal_2, "= 0")
elif getal_1 > getal_2:
        print("Het antwoord voor", getal_1, "en", getal_2, "is", getal_1)
else:
        print("Het antwoord voor", getal_1, "en", getal_2, "is", getal_2)