ingave = input("Geef een string: ")
lowerCase = ingave.lower()

if lowerCase[::-1] == lowerCase:
    print("{} is een palindroom".format(ingave))
else:
    print("{} is geen palindroom".format(ingave))