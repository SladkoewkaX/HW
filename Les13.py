# a = int(input("Введите число: "))
# def dlina(x):
#     res = []
#     for i in range(x):
#         if i % 2 == 0:
#             res.append(0)
#         else:
#             res.append(1)
#     return res
# print(dlina(a))

# def dlina(x):
#     res = []
#     for i in range(x):
#         if i % 2 == 0:
#             res.append(0)
#         else:
#             res.append(1)
#     return res
# print(dlina(9))

# def dlina(x):
#     res = []
#     for i in range(x):
#         res.append(i%2)
#     return res
# print(dlina(8))

#-------------------------------------
# a = [i for i in range(9) if i %4 ==0]  #i - то что добавиться в список, вместо append
# print(a)

# def dlina(x):
#     return [i%2 for i in range(x)]
# print(dlina(5))

# def dlina(x):
#     a = [i for i in range(x) if i %2 == 1]
#     b = [i for i in range(x) if i %2 == 0]
#     return a,b

# print(dlina(7))

# f = [y+x for x in range(6) for y in range(6,12)]
# print(f)

# f ={ x: y  for x in "ABC" for y in "ZXC" }
# print(f)

# f ={ x: y  for x,y in zip("ABC", "ZXC") }
# print(f)
