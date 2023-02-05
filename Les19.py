# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def voice(self):
#         pass
    
# class Lion(Animal):
#     def __init__(self, name):
#         self.name = name

#     def voice(self):
#         return "Raar"

# class Mouse(Animal):
#     def __init__(self, name):
#         self.name = name

#     def voice(self):
#         return "Pisk"

# simba = Lion("Simba")
# jerry = Mouse("Jerry")

# print(simba.voice())
# print(simba.name)
# print(jerry.voice())
# print(simba.name)
        
# my_num_list = [1,2,3,4,5]

# def a (num):
#     return num**2

# # print(a(5))

# c = map(a, my_num_list)
# print(list(c))

# list1 = (123,444,325,3423)
# def b (num):
#     return num + 2

# x = map(b, list1)
# print(list(x))

# my_num_list = [1,2,3,4,5]

# # my_func = a 
# # my_list = my_num_list

# def  a(num):
#     return num**2

# def map2(my_func, my_list):
#     result = []
#     for i in my_list:
#         result.append(my_func(i))
#     return result

# c = map2(a, my_num_list)
# print(list(c))


# my_num_list = [1,2,3,4,5]

# def a(num):
#     return num > 2

# my_list = filter(a,my_num_list)
# print(list(my_list))

# my_num_list = [1,2,3,4,5]

# def a(num):
#     return num > 2
# def a2(num, num2):
#     res = []
#     for i in num2:
#         if num(i):
#             res.append(i)
#     return res

# print(a2(a,my_num_list))

# my_num_list = [1,2,3,4,5]
# def a(num):
#     return num > 2
# def a2(num, num2):
#     return [i for i in num2 if num(i)]
# print(a2(a,my_num_list))



from hw17 import Bicycle

Bic = Bicycle(45 ,"black")
Bic.info()
print(Bic.info())