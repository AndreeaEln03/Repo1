myString = "Fiecare caracter are propriul sau index"
#print(len(myString))
#print(myString[0])
#print(myString[-1])
#print(myString[-3])
#print(myString[5: 8])
#print(myString[::-1])
print(myString[:-3])
slicedString = slice(2)
print(myString[slicedString])
print(myString[:2])
print(myString[0:2])
print(myString[3:-1])

#Exercitiu
# simularea unui bancomat

'''
simularea unui
bancomat
'''

expectedUserName = 'Costantea Andrei'
expectedParola = '2424'
sold = 200
# userName = input('User name: ')
# assert expectedUserName == userName, 'Username invalid'
# print("Username corect!")
#
# parola = input('Parola este: ')
# assert expectedParola == parola, 'Parola invalida'
# print('Parola corecta')
#
# plata = int(input('Suma de bani dorita: '))
# assert sold >= plata, 'Sold insuficient'
# print('Plata efectuata')

print('Sold = ' + str(sold))
# print(2+4)
# print('2' + '4')
print('----------------')
print(type(sold))
print(type(expectedUserName))
stringSold = '200'
print(type(stringSold))
assert  type(sold) == type(stringSold)

#Citim de la tastatura

nume = input('Popescu')
prenume = input('Andrei')
print(f'Numele complet are {len(nume)+ len(prenume)} caractere')