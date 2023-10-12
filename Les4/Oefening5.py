getallen = (1, 2, 3, 4, 5, 6, 4, 9, 8)
lijst = list(getallen)
i = 0

if 4 not in getallen:
    print(getallen)
    print("Het getal 4 komt niet voor in de Tuple")

while 4 in lijst:
    lijst.pop(0)

lijst = tuple(lijst)
print(getallen)
print(lijst)



