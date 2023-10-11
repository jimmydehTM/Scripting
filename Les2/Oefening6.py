is_ochtend = True
is_moeder = True
is_in_slaap = True

if is_in_slaap:
    print("Ik beantwoord geen telefoon")
elif is_ochtend and is_moeder:
    print("Hallo")
elif is_ochtend:
    print("Ik beantwoord geen telefoon")
else:
    print("Hallo")
    