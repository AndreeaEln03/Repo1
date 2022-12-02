# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(selfs):
#         raise NotImplementedError
#
#     @abstractmethod
#     def sleep(self):
#         raise NotImplementedError
#
# class Dog(Animal):
#     def sound(selfs):
#         print(' Ham Ham')
#
#     def sleep(self):
#         print('zZzzZ')
#
# class Cat(Animal):
#     def sound(selfs):
#         print('Miau miau ')
#
#     def sleep(self):
#         print('prrr')
#
# dog = Dog()
# dog.sound()
#
# cat = Cat()
# cat.sleep()


#incapsulare

class Car:
    __color ='gary'

    def _get_color(self):
        return self.__color

    def set_color(self, culoarea_dorita):
        self.__color = culoarea_dorita
        self.__message(f'Culoarea a fost schimbata in {culoarea_dorita}')

    def __message(self,message):
        print(message)
masina =Car()
masina.set_color('rosu')


class Triunghi():
    baza = 0
    inaltime = 0
    __arie = 0
    def __init__(self,baza ,inaltime):
        self.baza = baza
        self.inaltime = inaltime

    def getArie(self):
        return self.__arie

    def _calculateArie(self):
        self.__arie = self.baza * self.inaltime / 2
triunghi = Triunghi(7,4)
print(triunghi.getArie())