# a) Schrijf een programma dat de som maakt van alle getallen tussen 25 en 32 (inclusief de grenzen).
# b) Pas je programma aan zodat je ook zelf de begin- en eindgrens kan inlezen. Houd nu natuurlijk
# ook rekening met volgende situaties:
# • Begingrens en eindgrens zijn gelijk
# • Begingrens is groter dan de eindgrens

onder = int(input("Geef de begingrens: "))
boven = int(input("Geef de eindgrens: "))
totaal = onder



if boven == onder:
   print("Som van de getallen van", boven, "t.e.m.", onder)
   print(onder)
elif onder > boven:
   print("De begingrens moet kleiner zijn dan de eindgrens!")
else:
   print("Som van de getallen van", onder, "t.e.m.", boven)
   while onder < boven:
      optellen = onder + 1
      totaal += optellen
      print("+",optellen, '-->', totaal)
      onder +=1
   
   
   
   

    

