piesa_faina =True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par printam acest lucru
# altfel printam impar
nr = 3
# se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 2 == 0:
 print ('nr par')
else:
 print ('impar')
# este un numar pozitiv?
if (nr > 0):
 print ('pozitiv')
else:
 print( ' numar nu este pozitiv ')

# if, else if, else
# cum ne saluta robotelul in functie de ora
ora =int(input('Introdu ora'))
print(ora == 17)
if ora < 0:
 print('ora invalida')
elif ora <= 11:
  print( ' buna dimineata')
elif ora <= 21:
  print(' buna seara')
elif ora <= 24:
  print(' noapte buna')
else:
  print(' ora mai mare decat 24')
# ctrl+ /

# robotel telefonic
optiunea =int(input('alege o optiune'))
if optiunea ==0:
 print('meniu anterior')
elif optiunea == 1:
  print('ati ales romana')
elif optiunea == 2:
  print(' ati ales engleza')
else:
 print(' nu am indentificat optiunea ,mai departe')