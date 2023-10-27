ingave = input("Geef een string: ")

for i in range(len(ingave)-2):
    star = ingave.find('*')
    if star == -1:
        break
    else:
        ingave = ingave.replace(ingave[star-1:star+2], '')

print(ingave)