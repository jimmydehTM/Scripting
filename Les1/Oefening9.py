# Schrijf een programma waarmee je het aantal graden Fahrenheit (Tf) kan bereken als je zelf ingeeft hoe
# hoog de temperatuur is in graden Celsius (Tc) in. Gebruik deze omzettingsformule tussen Tc en Tf :

celcius = float(input("Geef het aantal graden Celcius: "))
FtoC = celcius * (9/5) + 32

print(celcius, "graden Celcius = ", FtoC, " graden Fahrenheit")