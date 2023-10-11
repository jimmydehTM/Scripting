# Oefening 8
# Schrijf een programma waarmee een gebruiker kan te weten komen om hoe laat zijn alarm zal
# afgaan als hij zelf aangeeft hoe laat het is (enkel het uur wordt ingegeven) en hoe lang hij wil
# wachten.
# Oefeningen Sequentie p. 3
# Bijvoorbeeld:
# het is 14u en hij wil 8u wachten het alarm zal afgaan om 22u
# het is 9u en hij wil 20u wachten het alarm zal afgaan om 5u


uur = int(input("Hoe laat is het? "))
wachten = int(input("Hoe lang wil je wachten? "))

if (uur + wachten) < 24:
    print("het is "+ str(uur) + "u en hij wil " + str(wachten) + 
          "u wachten het alarm zal afgaan om " + str(uur + wachten) + "u")
    
else: print("het is "+ str(uur) + "u en hij wil " + str(wachten) + 
            "u wachten het alarm zal afgaan om " + str((uur + wachten)-24) + "u")

