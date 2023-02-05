class Item:
    godnost = True 
    def __init__(self, name , cost , srok):
        self.name = name
        self.cost = cost
        self.srok = srok
    
    def cost1(self, s):
        self.cost = self.cost = s
    
    def srok1(self):
        self.godnost = False
    
    def percent1(self, percent):
        return self.cost - (self.cost/100*percent)
                

    def all(self):
        return f'Название: {self.name}, Цена: {self.cost}, Срок: {self.srok}, s : {self.godnost}'

item1 = Item("Бананы", None, 14 )
item1.cost1(int(input("Цена: ")))
print(item1.all())
item1.srok1()
print(item1.percent1(10))
print(item1.all())



# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b
    
#     def mult(self):
#         return self.a * self.b
    
#     def duv(self):
#         return self.a / self.b
    
#     def sub(self):
#         return self.a - self.b

# a = Math(45, 5)

# print(a.add())