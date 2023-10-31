import os

naam = input("Voer een naam in (enter om te stoppen): ")

while naam != '':
    print("Keuzemenu:")
    print("**********")
    print("H Hoofdletters")
    print("K kleine letters")
    print("A AfGeWiSsElD")
    print("**********")
    keuze = input("Maak je keuze (H-K-A): ")
    keuze = keuze.lower()
    while keuze != 'h' and keuze != 'k' and keuze != 'a':
        keuze = input("Maak je keuze (H-K-A): ")
        keuze = keuze.lower()
    
    if keuze == 'h':
        os.system('cls')
        print(naam.upper())
    if keuze == 'k':
        os.system('cls')
        print(naam.lower())
    if keuze == 'a':
        os.system('cls')
        lijst = list(naam)
        for i in range(0, len(lijst), 2):
            lijst[i] = lijst[i].upper()
        naam = ''.join(lijst)
        print(naam)
        
    naam = input("Voer een naam in (enter om te stoppen): ")
