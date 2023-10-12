lijst = [2, 4, 5, 9]
print(lijst)
aantal = len(lijst)
nullen = []
laatste_van_lijst = lijst[-1]
i = 0


while i < aantal*2:
    nullen.append(0)
    i += 1

nullen.pop(-1)
nullen.append(laatste_van_lijst)

print(nullen)