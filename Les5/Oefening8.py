ingave = input("Geef een string: ")

if ingave.find("aan") == -1:
    print("Aan komt niet voor")
elif ingave.find("aan") < 2:
    print("Aan komt voor op de eerste of tweede plaats")
elif ingave.find("aan") > 2:
    print("Aan komt voor maar niet vooraan in de string")