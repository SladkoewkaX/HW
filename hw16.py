# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type 
#         self.year = year
    
#     def metod1(self):
#         print ("Автомобиль заведен")
    
#     def metod2(self):
#         print ("Автомобиль заглушен")
    
#     def info(self):
#         return f'Год: {self.year}, Тип: {self.type}, Цвет: {self.color}'

# f = Car("Афроамериканский ", "Tesla", 1939)
# f.metod1()
# f.metod2()
# print(f.info())



class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type 
        self.year = year
    
    def metod1(self):
        self.metod1 = "Автомобиль заведен"
    
    def metod2(self):
        self.metod2 = "Автомобиль заглушен"
    
    def info(self):
        return f'1 start: {self.metod1}, 2 start: {self.metod2}, Год: {self.year}, Тип: {self.type}, Цвет: {self.color}'

f = Car(" Black ", "Tesla", 1939)
f.metod1()
f.metod2()
print(f.info())