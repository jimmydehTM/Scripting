naam = input("Voer een naam in (enter om te stoppen): ")
lijst = []

while naam != '':
    print("Keuzemenu:")
    print("**********")
    print("H Hoofdletters")
    print("K kleine letters")
    print("A aFgeWiSsElD")
    print("**********")
    keuze = input("Maak je keuze (H-K-A): ")
    keuze = keuze.lower()
    print(keuze)
    while keuze != ord(104) or keuze != 'k' or keuze != 'a':
        keuze = input("Maak je keuze (H-K-A): ")
        keuze = keuze.lower()
    if keuze == 'h':
        print(naam.upper())
    if keuze == 'k':
        print(naam.lower())
    if keuze == 'a':
        for i in naam:
            lijst.append[i]
            lijst[i].title()
    print(lijst)

