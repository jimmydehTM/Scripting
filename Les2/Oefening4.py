getal_1 = int(input("Geef een getal: "))
getal_2 = int(input("Geef nog een getal: "))
getal_3 = int(input("Geef nog een laatste getal getal: "))

if getal_1 > getal_2 and getal_1 > getal_3:
    if getal_2 + getal_3 == getal_1:
        print("Dit lukt")
    else: 
        print("Dit lukt niet")
elif getal_2 > getal_1 and getal_2 > getal_3:
    if getal_2 + getal_3 == getal_1:
        print("Dit lukt")
    else: 
        print("Dit lukt niet")
elif getal_3 > getal_1 and getal_3 > getal_2:
    if getal_2 + getal_3 == getal_1:
        print("Dit lukt")
    else: 
        print("Dit lukt niet")
 
