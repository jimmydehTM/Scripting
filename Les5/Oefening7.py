ingave = input("Geef een string: ")


aantal = 1
tussentijds = 1

for i in range(1, len(ingave)):
    if (ingave[i] == ingave[i - 1]):
        tussentijds += 1
    else:
        aantal = max(aantal, tussentijds)
        tussentijds = 1
 
    aantal = max(aantal, tussentijds)
 
 
print("De lengte van het grootste blok is", aantal)