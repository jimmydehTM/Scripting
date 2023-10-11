input_cijfer = int(input("Geef een getal: "))

if input_cijfer < 0:
    print("De test kan niet worden uitgevoerd.")
else:
    string = str(input_cijfer)
    getal = str(input("met welk cijfer wil je testen: "))
    last_char = string[-1]
    if getal == last_char:
        print(string, "eindigd inderdaad op", getal)
    else:
        print(string, "eindigd niet op", getal)