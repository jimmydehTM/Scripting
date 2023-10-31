import sys, os

spreekwoord = 'de kat krabt de krollen van de trap'
geraden = list(spreekwoord)

#make array with "#" accoring to unguess letters
for i in range(len(geraden)):
    if geraden[i] != chr(32):
        geraden[i] = "#"
os.system('cls')
print("dit spreekwoord moet je raden: ", (''.join(geraden)))

ingave = input("Raad een letter of druk / als je denkt de uitdrukking te kennen: ")

while True:
    os.system('cls')
    if ingave == '/':
        os.system('cls')
        antwoord = str(input("Ok, je denkt dat je het weet, zeg het maar: ")).lower()
        if antwoord == spreekwoord:
            print("Ja, je hebt gewonnen!")
            break
        elif antwoord != spreekwoord:
             print("Spijtig, je hebt verkeerd geraden!")
             ingave = input("Raad een letter of druk / als je denkt de uitdrukking te kennen: ")
    if ingave in spreekwoord:
        for i in range(len(spreekwoord)):
            if ingave == spreekwoord[i]:
                geraden[i] = ingave
    elif ingave not in spreekwoord:
        print("Dat is een foute letter!")
    os.system('cls')
    oplossing = '' .join(geraden)
    print("Dit resultaat heb je al: ", oplossing)
    if oplossing.find("#") < 0:
        os.system('cls')
        print("Je hebt het niet geraden!")
        print("De oplossing was:",spreekwoord )
        break

    ingave = input("Raad een letter of druk / als je denkt de uitdrukking te kennen: ")