lijst = [0, 45, 60, 13, 0, 42, 18, 17, 0, 26, 13]

for i in range(len(lijst) - 1):
    if lijst[i] == 0:
        x = i + 1
        while x < len(lijst):
            if lijst[x] % 2 != 0:
                lijst[i] = lijst[x]
                break
            x += 1

print(lijst)

