def cel_to_fahren(celcius):
    return celcius*(9/5)+32

ingave = float(input("Geef het aantal graden Celcius: "))

print("{} graden Celsius = {} graden Fahrenheit".format(ingave, cel_to_fahren(ingave)))