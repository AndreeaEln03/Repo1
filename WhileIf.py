# problema: masina merge cat timp inca are benzina

litri_benzina = 10
while litri_benzina > 0:
    #acceleram
    print('vruum vruum!')
    #scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print(" beculetul rosu")
print('Stop!')


#dalmatienii
for i in range(1,102):
    print(f'Dalmatianul cu nr {i}')

#dalmatienii din 2 in 2
for i in range (1,102,2):
    print(f'Dalmatianul cu nr {i}')

numere = [3,7,10]
#parcurgere lista cu for prin intermediul indexului
for i in range(0,len(numere)):
    print(f'indexl curent este {i}')
    print(f'numarul curent este {numere[i]}')


# for each
s=0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
print(f'Suma este {s}')