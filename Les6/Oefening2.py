def euro_to_dollar(euro, change):
    return euro*change

ingave_bedrag = float(input("Geef de bedrag in Euro: "))
ingave_dollarkoers = float(input("Geef de huidige dollarkoers: "))

print("{}Euro = ${}".format(ingave_bedrag, euro_to_dollar(ingave_bedrag, ingave_dollarkoers)))