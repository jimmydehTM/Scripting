# Schrijf een programma om een bedrag in Euro om te zetten in Dollar. Je moet de wisselkoers van de dag
# zelf ook eerst inlezen.

Koers = float(input("Geef de huidige koers: "))
bedrag = int(input("Geef het bedrag in euro: "))
print(bedrag,"Euro = ", (bedrag*Koers),"Dollar")