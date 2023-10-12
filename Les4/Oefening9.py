ingave = input("Geef een tekst: ")
lijst = []
i = 0
x = 0

while len(ingave) > 0 and i < len(ingave):
    if ingave[i] != " ":
        lijst.append(ingave[i])
    i+=1



lijst = set(lijst)
lijst = list(lijst)
lijst.sort()
print(lijst)