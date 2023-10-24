lijst = [0, 45, 60, 13, 0, 42, 18, 17, 0, 26, 13]
b = []
i = 0


while i < len(lijst):
    for i in len(lijst):
        if lijst[i] == 0:
            z = lijst[i+1]
            x = lijst.pop(lijst[i])
            lijst.insert(x, z)
        
        
        
    i+=1

print(lijst)