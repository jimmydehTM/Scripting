ingave = list(input("Geef een string: "))

for i in range(0,len(ingave)-2,3):
    letter = ingave.pop(i)
    ingave.insert(i+2, letter)
    i+3

woord = ''.join(ingave)

print(woord)