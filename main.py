from vehicles import Car, Truck, GasolineEngine


def main():
    engine_1 = GasolineEngine()
    engine_2 = GasolineEngine()
    engine_3 = GasolineEngine()
    car_1 = Car(engine=engine_1, color="red")
    car_2 = Car(engine=engine_2, color="blue")
    truck = Truck(engine=engine_3, color="green")

    vehicles = [car_1, car_2, truck, 1, "text"]

    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            print(vehicle.drive())
        else:
            print("not a car")


if __name__ == '__main__':
    main()
