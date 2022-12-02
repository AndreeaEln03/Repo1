from OOP import Car

class Service:
    listCar=[]
    numberOfCar = 0
    price = 0

    def __init__(self):
        pass
    def  setListCar(self,listCar):
         self.listCar = listCar

    def  getNumberOfCars(self):
         self.numberOfCar = len(self.listCar)
         return self.numberOfCar

    def setPrice(self,price):
        self.price = price

    def calculatePrice(self):
        for x in self.listCar:
            if x.model == 'Logan':
                print('Pretul este 3000 de lei')
                self.setPrice(3000)
            elif x.model == 'Sandero':
                print('Pretul este de 4000 de lei ')
                self.setPrice(4000)
            else:
                print('Pretul este de 2500 de lei')
                self.setPrice(2500)


car1 = Car('Logan','negru')
car2 = Car ('Sandero' ,'rosu')
car3 = Car ('Duster', 'alb')
car4 = Car ('Logan','alb')
service = Service()
service.setListCar([car1, car2 ,car3,car4])
service.getNumberOfCars()
service.calculatePrice()

print(service.getNumberOfCars())