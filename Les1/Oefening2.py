# Oefening 2
# Schrijf een programma waarmee een gebruiker de resultaten van een stemming kan omvormen tot
# percentages. De gebruiker voert het aantal Ja stemmen, het aantal Nee stemmen en het aantal
# blanco stemmen in. Het programma toont het percentage van elk soort stemmen.


Ja_stemmen = int(input("Geef het aantal 'JA' Stemmen: "))
Nee_stemmen = int(input("Geef het aantal 'Nee' Stemmen: "))
Blanco_stemmen = int(input("Geef het aantal 'Blanco' Stemmen: "))



Aantal_stemmen =  Ja_stemmen + Nee_stemmen + Blanco_stemmen

Percentage_ja = (Ja_stemmen / Aantal_stemmen) * 100

Percentage_nee = (Nee_stemmen / Aantal_stemmen) * 100

Percentage_blanco = (Blanco_stemmen / Aantal_stemmen) * 100


print("Aantal ja-stemmen:",Ja_stemmen)
print("Aantal neen-stemmen:",Nee_stemmen)
print("Aantal blanco-stemmen: ",Blanco_stemmen)
print("Ja: ",Percentage_ja,"%")
print("Nee: ",Percentage_nee,"%")
print("Blanco: ",Percentage_blanco,"%")
      