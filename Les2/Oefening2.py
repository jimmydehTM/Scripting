geboortejaar = int(input("Geef je geboortejaar: "))
leeftijd = 2023 - geboortejaar

print("Je leeftijd =", leeftijd)
if leeftijd > 17:
    print("Je bent volwassen.")
else:
    print("Je bent nog niet volwassen.")