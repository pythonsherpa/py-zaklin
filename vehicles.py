class Engine:
    pass


class GasolineEngine(Engine):
    pass


class DieselEngine(Engine):
    pass


class Vehicle:
    def __init__(self, engine: Engine, color):  # engine -> Composition
        self.engine = engine
        self.color = color

    def drive(self):
        return "Driving the vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving the car"


class Truck(Vehicle):
    pass


class MotorBike(Vehicle):
    pass


class CustomInteger(int):
    def double(self):
        return self * 2


class CustomString(str):
    def double(self):
        return self * 2
