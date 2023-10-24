ingave = input("Geef een string: ")

i=0
triples = 0
while i < len(ingave)-2:
    if len(ingave) < 3:
        break
    else:
        if ingave[i] == ingave[i+1]:
            if ingave[i] == ingave[i+2]:
                triples +=1
    i+=1

if len(ingave) < 3:
    print("Deze ingave is te kort.")
if triples == 1:
    print("Er is 1 triple in deze string")
if triples > 1:
    print("Er zijn {} triples in deze string".format(triples))
if triples == 0:
    print("Er zijn geen triples in deze string")