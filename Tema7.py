from abc import abstractmethod

# ABSTRACTION


class FormaGeometrica():
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica


# ENCAPSULATION

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Am sters latura')
        self.__latura = None

    def aria(self):
        print(f'Aria este: {self.__latura * self.__latura}')

#Obiect Patrat

patrat = Patrat(4)
patrat.latura
patrat.aria()
patrat.latura = 6
patrat.latura
# del patrat.latura
# patrat.latura
patrat.aria()
patrat.descrie()

# Clasa Cerc
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Noua raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters raza')
        self.__raza = None

    def aria(self):
        print(f'Aria este: {self.__raza * self.__raza * FormaGeometrica.PI}')

    # POLYMORPHISM

    def descrie(self):
        print('Eu nu am colturi')



cerc = Cerc(4)
cerc.raza
cerc.aria()
cerc.raza = 2
cerc.raza
cerc.aria()
del cerc.raza
cerc.raza
cerc.descrie()