def printGreeting():
    print('Buna ziua!Bine ati venit!')

def printGretingByName(nume,prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a,b,c):
    return(a + b + c) /3

def piValue():
    return 3.14

# exercitiu
# daca persoana e majora astfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

#zona de apelare (desktop)
printGreeting()
printGreeting()
printGretingByName('Ioan','Alexandru')
printGretingByName('Ioan','Maria')
printGretingByName('Ioan','Alina')
print(mediaNr(3,3,4,))
print(piValue())
print(verificareMajor(18))

# se ia varsta utilizatorului
age = int(input('introduceti varsta'))
if verificareMajor(age):
    print('Cont creat .Bine ai venit in aplicatie')
else:
    print('Nu ai varsta minima necesara(18)pentre a paria')