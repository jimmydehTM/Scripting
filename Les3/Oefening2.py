# Schrijf een programma om te tellen uit hoeveel nullen en zessen een ingegeven getal bestaat. Test
# met echte getallen. Deze starten dus niet met het cijfer 0. Voer je toch een getal in startend met het
# cijfer 0, valt deze uiteraard weg. 0125 wordt in het geheugen immers gestockeerd als 125.

getal = int(input("Geef een getal: "))
nullen = 0
zessen = 0

while(getal > 0):
 
    eind_getal = getal % 10
    print(eind_getal)
    if(eind_getal == 0):
        nullen += 1
    if(eind_getal == 6):
        zessen += 1
    getal //= 10


# for i in range(0, len(getal)):
#     if getal[i] =='0':
#         nullen += 1
#     elif getal[i] == '6':
#         zessen += 1
        
print("Het getal bestaat uit", nullen, "nullen en", zessen, "zessen.")
