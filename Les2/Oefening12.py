# Blad, steen, schaar is een spel voor 2 spelers. De spelers kiezen tegelijk één van de mogelijkheden
# steen, schaar of blad. Steen verslaat de schaar (de schaar wordt bot), blad verslaat steen (pakt de
# steen in) en schaar verslaat blad (knipt het stuk). Als beide spelers dezelfde keuze maken, is het
# gelijkspel.
# Leg de keuze van de computer zelf vast in je programma. Laat de speler één van de drie
# mogelijkheden steen, schaar of blad kiezen en bepaal dan wie er wint.


from random import randint

value = randint(0, 2)
lijst = ["blad", "steen", "schaar"]

speler = input("Blad, steen of schaar? ")

computer = lijst[value]

print("Speler koos", speler, "\n" + "Computer koos", computer)

if computer == speler:
    print("Gelijk spel!")
elif (computer == "blad" and speler == "schaar") or (computer == "steen" and speler == "blad") or (computer == "schaar" and speler == "steen"):
    print("Speler wint!")
else: print("Computer wint!")