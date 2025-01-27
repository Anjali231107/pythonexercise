class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        def move(self) :
            print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail!")

class Plane(vehicle):
    def move(self):
        print("fly!")

car1 = Car("Ford", "mustang")
boat1 = Boat("anjali", "aryal")
plane1 = Plane("baudha", "yeti")

for x in (car1, boat1, plane1):    
    print(x.brand)
    print(x.model)
    x.move() 