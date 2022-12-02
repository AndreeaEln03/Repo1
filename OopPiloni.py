#exceptii
# try:
#     lista =[1,2,3]
#     lista[6]
#
# except IndexError as e :
#     print(e)
# print('Am ajuns aici')
#
# raise IndexError('Eroare fortata')

# mostenire
# class Chef:
#     def make_salas(self):
#         print('Chef : salad')
#
#     def make_fries(self):
#         print('fries')
#
# class JapaneseChef(Chef):
#     def make_sushi(self):
#         print('sushi')
#     def make_salas(self):
#         print('Japanese Chef: salad')
#
# class ItalianChef(Chef):
#     def make_pizza(selfs):
#         print('pizza')
#
# chef =Chef()
# japaneseChef= JapaneseChef
# italianChef= ItalianChef
#
# chef.make_fries()
# japaneseChef.make_sushi()
# italianChef.make_pizza()
# japaneseChef.make_salas()




#polimorfism
print(len('abc'))
print(len([1,2,3,4]))


def add(x,y,z=0):
    return x + y + z

print(add(2,3))
print(add(2,3,5))
# 5
# class Adunare():
#     def add(self x,y):
#         return x + y
#
#     def add(self x, y ,z=0):
#         return x + y + z
# adunare = Adunare()
# print(adunare.add(3,5,6))
#


