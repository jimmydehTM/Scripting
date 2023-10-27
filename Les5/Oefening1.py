ingave = input('Geef een kleur: ')
i = 0
print('{}{}'.format(ingave[0], ingave[2]))
print('Deze kleur bestaat uit {} letters.'.format(len(ingave)))
print()


for letter in ingave:
    print('{} = {}'.format(letter,ord(letter)))

print()

while i < len(ingave):
    if i < 1 or i % 2 == 0:
        print('#{}#'.format(ingave[i]))
    else: 
        print('**{}**'.format(ingave[i]))
    i += 1