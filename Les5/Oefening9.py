ingave = "dddddbroodjambrood"

if ingave.index('brood') > 0:
    ingave = ingave[ingave.index('brood'):]
    ingave = ingave.replace('brood','')
elif ingave.count('brood') < 2:
    print("")
else: 
    ingave = ingave.replace('brood','')

print(ingave)