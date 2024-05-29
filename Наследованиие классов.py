class Car:
    price = 1000000

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} - price:{}'.format(self.__class__.__name__, self.price)

    def horse_powers(self):
        print('150 horsepower')


class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        print('140 horsepower')


class Kia(Car):
    price = 800000

    def horse_powers(self):
        print('110 horsepower')


car1 = Nissan(name=None)
car2 = Kia(name=None)
print(car1)
car1.horse_powers()
print(car2)
car2.horse_powers()