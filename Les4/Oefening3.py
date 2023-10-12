scores = []
totaal = 0

print("Geef de score voor de test. Gebruik -1 als je wil afsluiten: ")
ingave = float(input("score: "))

while ingave > 0:
    scores.append(ingave)
    totaal +=1
    ingave = float(input("score: "))


scores.sort()
print("De scores in de gesorteerde volgorde ", scores)
gemiddelde = sum(scores) / len(scores)
print("Het gemiddelde van de", totaal, "scores = ", gemiddelde)

