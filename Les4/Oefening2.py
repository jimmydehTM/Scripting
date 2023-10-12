lijst = [9, 17, 25, 4, 12, 7]
i = 0
while i < len(lijst):
    if lijst[i] % 2 == 0:
        b = lijst[i]
        lijst.remove(lijst[i])
        lijst.insert(0, b)
    i+=1
print(lijst)