# Oefening 3
# Schrijf een programma waarmee je een getal van 3 cijfers inleest en van dit getal afdrukt:
# - De helft
# - Het dubbel
# - De derde macht
# - Het tienvoud
# - Alle afzonderlijke cijfers van het getal


getal = int(input("Geef een getal met 3 cijfers: "))
text = str(getal)

print("De helft: ", (getal / 2))
print("Het dubbel: ", (getal * 2))
print("De derde macht: ", (getal ** 3))
print("Het tienvoud: ", (getal * 10))
print("De cijfers zijn: ")
print(text[:1])
print(text[1:2])
print(text[2:3])