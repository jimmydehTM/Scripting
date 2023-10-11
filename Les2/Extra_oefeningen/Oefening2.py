# a) Schrijf een programma waarmee je kan nakijken of het rijksregisternummer dat iemand
# doorgeeft correct is. Zoek zelf op wat de betekenis is van de verschillende onderdelen van je
# rijksregisternummer en print dan de volgende informatie af.
# b) Breid je programma uit zodat de maand van de geboortedatum in tekstvorm verschijnt dus in
# het voorbeeld wordt dat: 4 oktober 59.


naam = input("Geef je naam: ")
eerste_cijfers = int(input("Geef de eerste 9 cijfers van je rijksregisternummer: "))
laatste_cijfers = int(input("Geef de laatste 2 cijfers van je rijksregisternummer: "))
jaar = str(eerste_cijfers)[0:2]
maand = str(eerste_cijfers)[2:4]
dag = str(eerste_cijfers)[4:6]
geslacht_getal = str(eerste_cijfers)[6:9]

controlegetal = eerste_cijfers % 97
restcijfer = 97 - controlegetal

if int(geslacht_getal) % 2 == 0:
    geslacht = "vrouwelijk"
else: geslacht = "mannelijk"

    


if laatste_cijfers != restcijfer:
    print("Dag" + naam + ", het rijksregisternummer dat je doorgaf is niet correct!")
else: print("Dag" + naam + ", Je bent van het " + geslacht + " geslacht. En je bent geboren op: " + dag + "/" + maand + "/" + jaar)