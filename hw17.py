class Bicycle:
    def __init__(self, speed ,color, wheel=2):
        self.speed = speed
        self.wheel = wheel
        self.color = color

    def info(self):
        return f'Скорость: {self.speed}, Кол-во колес: {self.wheel}, Цвет: {self.color}'

from hw17 import Bicycle

Bic = Bicycle(45 ,"black")
Bic.info()
print(Bic.info())