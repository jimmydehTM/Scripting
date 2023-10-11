getal_1 = int(input("Geef een getal: "))
getal_2 = int(input("Geef nog een getal: "))
getal_3 = int(input("Geef nog een laatste getal getal: "))

if getal_1 < getal_2 and getal_1 < getal_3:
    print(getal_1 , "is het kleinste getal.")
elif getal_2 < getal_1 and getal_2 < getal_3:
    print(getal_2 , "is het kleinste getal.")
else: print(getal_3, "is het kleinste getal.")