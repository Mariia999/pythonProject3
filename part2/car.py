class Driver:
    def __init__(self, fullName, drivingExperience):
        self.fullName = fullName
        self.drivingExperience = drivingExperience

    def __str__(self):
        return f'Driver {self.fullName} have driving experience {self.drivingExperience} year(s)'

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

    def __str__(self):
        return f'power {self.power} - manufacturer {self.manufacturer}'

class Car:
    def __init__(self, carBrand, carClass, weight, driver: Driver, engine: Engine):
        self.carBrand = carBrand
        self.carClass = carClass
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print(f'{self.carBrand} started')

    def stop(self):
        print(f'{self.carBrand} stopped')

    def turnRight(self):
        print(f'{self.carBrand} turned right')

    def turnLeft(self):
        print(f'{self.carBrand} turned left')

    def __str__(self):
        return f'car Brand - {self.carBrand}, carClass - {self.carClass}, \
        weight - {self.weight}, driver - {self.driver}, engine - {self.engine}'


class Lorry(Car):
    def __init__(self, carBrand, carClass, weight, driver: Driver, engine: Engine, loadCapacity):
        super().__init__(carBrand, carClass, weight, driver, engine)
        self.loadCapacity = loadCapacity

class SportCar(Car):
    def __init__(self, carBrand, carClass, weight, driver: Driver, engine: Engine, maxSpeed):
        super().__init__(carBrand, carClass, weight, driver, engine)
        self.maxSpeed = maxSpeed