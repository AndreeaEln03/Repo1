class Car:
    make = 'Dacia'
    model = None
    year = 2022
    color = None

    def __init__(self, model_param,color):
        self.model = model_param
        self.color = color

    def getfield(self):
        print(self.color)
        print(self.model)
        print(self.year)
        print(self.make)

Car1= Car('Logan','negru')
Car2 = Car ('Duster','rosu')
Car1.getfield()
Car2.getfield()


#Car1.accelerate()
#Car2.stop()