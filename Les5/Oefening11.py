ingave = input("Geef een string: ")

x = ingave.count("x")
y = ingave.count("y")

if ingave.index("x") > ingave.index("y") or x != y:
    print("In de gegeven tekst zijn x en y NIET in evenwicht.")
elif x == y:
    print("In de gegeven tekst zijn x en y in evenwicht")