# joc de noroc cu zar
# avem un zar cu 6 fete
# trebuie sa scriem un nr si verificam daca nr egal cu fata zarului aruncat

import random
zar =[1, 2, 3, 4, 5, 6,]

diceRoll = random.choice(zar)

numar_Ales =int(input('Alege un numar:'))

if numar_Ales < diceRoll:
    print(f'Ai pierdut!Ai ales un numar mmai mic .Ai ales {numar_Ales}, dar a fost {diceRoll}')
elif numar_Ales > diceRoll:
    print(f'Ai pierdut! Ai ales un numar mai mare .Ai ales {numar_Ales}, dar a fost {diceRoll} ')
else:
    print('Ai castigat ! Felicitari')
