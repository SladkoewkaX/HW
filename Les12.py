# def add(a,b=4):
#     try:
#         return a+b
#     except TypeError:
#         print("Нельзя")
        
# print(add(1, "a"))


# def num(x,y):
#     res = []
#     for i in x:
#         if i in y and i not in res:
#             res.append(i)      
#     return res
# my_set = [1,2,3,4,5,5,2,6]
# my_set1 = [1,2,3,7,8,9]
# print(num(my_set,my_set1))






# def num(q,w):
#     for i in w.keys():
#         if i not in q.keys():
#             q[i]=w[i]
#     return q
# my_dict = {'a':1, 'b': 3, 'c': 5}
# my_dict1 = {'a':1, 'b': 3, 'g': 5}
# print(num(my_dict,my_dict1))



# a = int(input("Введите координаты: "))
# b = int(input("Введите вторую координатy: "))
# def x(a,b):
#     if a > 0 and b > 0 :
#         return "Правый верх"
#     elif a > 0 and b < 0:
#         return "Правый низ"
#     elif a < 0 and b < 0:
#         return "Левый верх"
#     elif a < 0 and b < 0:
#         return "Левый низ"
# print(x(a,b))
