
def druk_vierkant(aantal, teken):
    lijn = ''
    for i in range(aantal):
        lijn += teken
    for i in range(aantal):
        print(lijn)    
    
input_teken = input("Geef het teken waarmee de lijnen gevormd worden (enter = stop): ")

while input_teken != '':
    input_aantal = int(input("Geef een aantal: "))
    druk_vierkant(input_aantal, input_teken)
    input_teken = input("Geef het teken waarmee de lijnen gevormd worden (enter = stop): ")

