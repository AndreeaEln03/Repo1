#listele in pyton pot sa cuprinda elemente de tipuri diferite
# au dimenisiune dinamica
fructe = ['mar','banana', 'portocale', 3, True]

# afisam o lista
print(fructe)

# acesam  un element in functie de index
print(fructe[1])

#adaugam un nou element
fructe.append('capsuna')

#suprascriere
fructe[0]= 'para'

#afisam lista
print(fructe)

#aflam diminensiunea
print(len(fructe))

#scoate si ne retureneaza ultimul element
last = fructe.pop()
print('ultimul element', last)
print('lista: ', fructe)


#de cete ori apare un element
print(fructe.count(3))

fructe_exotice =['ananas ', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)