# def contBancar(userName, parola,sold):
#     i = 0
#     while i < 3:
#       if userName == 'Bogdan Alexa':
#             if parola == '2231':
#                 if sold < 200:
#                     print('Tranzactie reusita')
#                     break
#                 else:
#                     print('Fonduri insuficiente')
#                     break
#             else:
#                 print('Parola gresita')
#                 parola = input('Parola:')
#     else:
#         print('Username gresit!')
#         userName = input('ID:')
#         i +=1
#     print('Multumim .O zi frumoasa!')
#
# contBancar(input('Id:'),input('Parola:'),int(input('Sold:')))


# def bubblesort(lista):
#     for i in range(len(list) - 1):
#         for j in range(len(list)-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1]= list[j+1],list[j]
#     return(list)

# listaSortata = bubblesort([3,6,8,1,4,9,0,10])
# print(listaSortata)

#
# def listaMax(lista):
#    listaSortata = bubblesort(lista)
#    return listaSortata[-1]
# maxim = listaMax([3,6,8,1,4,9,0,10])
# print(maxim)
#
# def listaMaxx2(lista):
#     maxim = 0
#     for i in range(len(lista)):
#         if maxim < lista[1]:
#             maxim = lista[1]
#     return maxim
# maxim = listaMax([3, 6, 8, 1, 4, 9, 0, 10])
# print(maxim)


# import random
# def diceRool():
#     zar =[1, 2, 3, 4, 5, 6,]
#     numarZar = random.choice(zar)
#     numarAles =int(input('Alege un numar:'))
#     if numarAles < numarZar:
#         print(f'Ai pierdut! Ai ales un numar mai mic .Ai ales{numarAles}, dar a fost')
#     elif numarAles > numarZar:
#         print(f'Ai pierdut !Ai ales un numar mai mare .Ai ales {numarAles}, dar a fost')
#     else:
#         print('Ai catigat ! Felicitari!')


import ExIfElse_2
ExIfElse_2.diceRoll