# list1=[10,20,30,'alex' ,'andrei',50]
# print(list1)
# print(len(list1))
# list1.remove(10)
# print(list1)
# list1.remove(list1[0])
# print(list1)
# list1.pop(0)
# print(list1)
# list1.extend([1,2,3,4])
# print(list1)
# list1 =list1 +[1,2,3,4,]
# print(list1)
# list1.append('string')
# print(list1)
# list1.insert(2,2)
# print(list1)
# lista2=[4,4,6,]
# lista2.extend(list1)
# print(lista2)
# lista2.insert(3,list1)
# print(lista2)

#Dictionare
# dictionar={'fructe' : 'par', 'legume': 'morcov'}
# print(dictionar)
# print(dictionar.values())
# print(dictionar.keys())
# dictionar.update({2: 'luni'})
# print(dictionar)
# print(dictionar.get(2))
# val=dictionar.pop(len(dictionar)-1)
# print(val)
# print(dictionar)

#seturi

masini={'opel','volvo',2,3}
masini2={'opel','audi',5,6}
print(masini)
print(masini.intersection(masini2))
print(masini.difference(masini2))
masini.update([5,6,7,8])
print(masini)
print(type(masini))
newSet = set()
newSet.update({2,8,9})
print(newSet)

#tuple

zile= ('luni','marti','miercuri')
print(zile)
luni='mai','iunie','iulie'
print(luni)
print(type(luni))
mai,iunie,iulie =luni
print(mai,iunie,iulie)
mai2,_,_=luni
# saptamana = ('luni','marti',('miercuri','joi'))
print('saptamana')
print('saptamana[2][1]')