lijst = ['kat', 'hond', 'muis', 'rat', 'eekhoorn', 'uil', 'mol']
print(lijst)


eerste = lijst[0]
laatste = lijst[-1]
lijst.pop(0)
lijst.pop(-1)
lijst.insert(0, laatste)
lijst.insert(6, eerste)

print(lijst)