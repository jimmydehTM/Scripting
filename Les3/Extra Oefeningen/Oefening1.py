# Vooraf: om dit spel te programmeren zal je moeten gebruik maken van de mogelijkheden die Python
# biedt om een willekeurig getal te genereren. Lees daarom eerst na op hoe de methode randint
# werkt. https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
# Experimenteer even om te checken of je goed begrijpt hoe de methode werkt.
# In het volgende spel maakt de computer 2 hoopjes van een willekeurig aantal lucifers, maar wel
# minstens 20 en maximaal 40 per hoopje. De speler weet niet hoeveel lucifers er op elk hoopje liggen.
# Het spel gaat als volgt: om de beurt mogen de speler en de computer van één van beide hoopjes een
# aantal (minimum 3, maximum 8) lucifers nemen. Diegene die de laatste lucifer neemt van een
# hoopje, wint het spel.
# De speler zal telkens moeten zeggen hoeveel lucifers hij neemt en van welk hoopje hij lucifers neemt.
# Hij moet dit doen zonder te weten hoe groot de hoopjes nog zijn.
# De computer doet achteraf hetzelfde maar die maakt zijn keuze willekeurig (random).
# Op het einde druk je af:
# • ‘Joepie, ik win’, als de computer het spel wint.
# • ‘Proficiat, jij wint’, als de speler het spel wint.


import random as rand

hoopje_1 = rand.randint(20,40)
hoopje_2 = rand.randint(20,40)


while hoopje_1 > 0 or hoopje_2 > 0:
    
    keuze_speler_hoopje = int(input("Van welk hoopje neem je? "))
    keuze_speler_lucifers = int(input("Hoeveel lucifers (tussen 3 en 8) neem je? "))
    computer_hoopje = rand.randint(1,2)
    computer_lucifer = rand.randint(3,8)
    if keuze_speler_hoopje == 1:
        hoopje_1 -= keuze_speler_lucifers
    if hoopje_1 < 1:
        print("Proficiat jij wint!")
        break
    if keuze_speler_hoopje == 2:
        hoopje_2 -= keuze_speler_lucifers
    if hoopje_2 < 1:
        print("Proficiat jij wint!")
        break
    if computer_hoopje == 1:
        hoopje_1 -= computer_lucifer
    if hoopje_1 < 1:
        print("Joepie ik win!")
        break
    if computer_hoopje == 2:
        hoopje_2 -= computer_lucifer
    if hoopje_2 < 1:
        print("Joepie ik win!")
        break
    