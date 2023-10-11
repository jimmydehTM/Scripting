# a) Schrijf een programma waarmee de gebruiker de getallen tussen 10 en 20 kan afdrukken, waarbij
# het getal 10 ook 10 keer wordt afgedrukt enz.

a = 10

while a <= 20:
    for i in range(a):
        print(a, end=" ")
    print()
    a +=1

    