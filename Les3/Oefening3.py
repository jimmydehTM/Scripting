# Schrijf een programma waarin je de leeftijd van een vader en een zoon inleest. Bereken dan hoe oud
# ze zullen zijn als de vader exact 2x zo oud is dan de zoon.
# Houd er rekening mee dat voor sommige vader-zoon combinatie dit niet meer mogelijk is.

zoon = int(input("Hoe oud ben jij: "))
vader = int(input("Hoe oud is je vader: "))
jaren = 0

while vader/2 != zoon:
    zoon += 1
    vader += 1
    jaren += 1
    
    
print("Binnen", jaren, "is je vader dubbel zo oud als jij.")
print("Je vader is dan", vader, "en jij", zoon)
