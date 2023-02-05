# def summa(c):
#     def summa1(*args):
#         func = c(*args)
#         res = []
#         for i in args[0]:
#             if i > 5:
#                 res.append(i)
#         return func, res
#     return summa1
# @summa
# def x(c):
#     return sum(i for i in c)
# s = (1,2,3,4,5,6,7,8,9,10)
# print(x(s))


# def summa(c):
#     def summa1(*args):
#         func = c(*args)
#         d = sum(args[0])
#         print (d)
#         return func
#     return summa1
# @summa
# def x(c):
#     one = []
#     for i in c:
#         if i > 5:
#             one.append(i)
#     return one
# s = (1,2,3,4,5,6,7,8,9,10)
# print(x(s))

# ------------------------------
# def a(w,d,*args):
#     print(w)
#     print(d)
#     print(args)
# b = [1,2,3,4,5,6,7]
# a(*b)

# def a(*args, **kwargs):
#     print(kwargs)
#     print(args)

# b = [1,2,3,4,5,6,7]

# a(*b , r =6 , y=8)

# def a(**kwargs):
#     print(kwargs)

# d = {'y': 6, 'z':7}
# a(**d)

# def a(y,z):
#     print(y)
#     print(z)

# d = {'y': 6, 'z':7}
# a(**d)
# -----------------------------

# from faker import Faker
# # fake = Faker(('Ru_RU'))  #['it_IT', 'en_US', 'ja_JP']
# fake = Faker
# def number1(x):
#     a = []
#     for i in range(5):
#         a.append({'name': fake.name(), 'email':fake.email(), 'city': fake.city()})
#     return a
# print(number1(None))