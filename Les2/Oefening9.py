# Lees drie getallen a, b en c in, die allemaal gelijk zijn aan 0, 1 of 2.
# Bepaal nu het testresultaat en druk dat af.
# Als de drie getallen gelijk zijn aan 2 dan is het resultaat 10. Als ze wel alle drie gelijk zijn maar niet aan
# 2 dan is het resultaat 5.
# In het andere geval: als de getallen b en c verschillend zijn van a dan is het resultaat 1. In alle andere
# gevallen is het resultaat 0.

getal_1 = int(input("Geef een getal (0,1,2): "))
if getal_1 > 2:
    print("verkeerd getal")
getal_2 = int(input("Geef nog een getal (0,1,2): "))
if getal_2 > 2:
    print("verkeerd getal")
getal_3 = int(input("Geef een laatste getal (0,1,2): "))
if getal_3 > 2:
    print("verkeerd getal")
else:
    if getal_1 == 2 and getal_2 == 2 and getal_3 == 2:
        print("10")
    elif getal_1 == getal_2 and getal_2 == getal_3:
        print("5")
    elif getal_1 != getal_2 and getal_1 != getal_3:
        print("1")
    else: print("0")