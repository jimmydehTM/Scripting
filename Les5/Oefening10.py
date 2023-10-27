i = 1
lijst = []

while i < 6:
   ingave = input("Geef woord {}: ".format(i)).capitalize()
   lijst.append(ingave)
   i += 1
lijst.reverse()

print(' '.join(lijst))