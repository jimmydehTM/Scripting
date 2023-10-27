
getallen = (4, 2, 3, 7, 5, 6, 1, 9, 8)
lijst = list(getallen)


if 4 not in getallen:
    print(getallen)
    print("Het getal 4 komt niet voor in de Tuple")

else: 
    while 4 in lijst:
     lijst.pop(0)

    lijst = tuple(lijst)
    print(getallen)
    print(lijst)




