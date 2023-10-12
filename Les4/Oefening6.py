student_lijst = []
student_afstand = []
aantal = 0

print("Geef je naam en je afstand naar school.")
print("Typ stop als naam wanneer je de invoer wenst af te sluiten.")
naam = input("Je naam: ")
    
while naam != 'stop':
    afstand = float(input("Afstand naar school: "))
    student_lijst.append(naam)
    student_afstand.append(afstand)
    naam = input("Je naam: ")
    aantal +=1

if len(student_lijst) > 0:
    print("Overzicht")
    verste = student_afstand.index(max(student_afstand))
    for i in range (len(student_afstand)):
        print(student_afstand[i], student_lijst[i])
    print(student_lijst[verste], "woont het verst, namelijk", max(student_afstand))
    print("De gemiddelde afstand is", (sum(student_afstand)/2))