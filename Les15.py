# def a(*args, **kwargs):
#     print(args)
#     print(kwargs)

# a(12,34, a=12)

# def a(a,b,*args):
#     print(a)
#     print(b)
#     print(args)

# a(1,2,3,4,5,6,7)

# def a(*args):
#     print(args)
# b = [1,2,4,5,6,7]
# a(*b)

# def a (**kwargs):
#     print(kwargs)
# s = {'s':3, 'f':4}
# a(**s)

# def a (s,f,**kwargs):
#     print(s)
#     print(kwargs)
# s = {'s':3, 'f':4, 'r':5}
# a(**s)

# def a(*args, **kwargs):
#     print(kwargs)
#     print(args)
# s = {'s':3, 'f':4, 'r':5}
# a(*[1,2,3,4,5],**s)
# ------------------------------

# def a(*args):
#     summ = 0
#     for x in args:
#         summ += x
#     return summ
# s = [1,2,3,4,5]
# print(a(*s))

# ------------------------------


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         print(function.__name__)
#         return func
#     return wrapper

# @uppercase_decorator
# def say_hi():
#     return "hello there"
# print(say_hi())



# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# def say_hi():
#     return "hello there"
# decorate = uppercase_decorator(say_hi)
# print(decorate())

def uppercase_decorator(function):
    def wrapper(*args, **kwargs):
        func = function(*args, **kwargs)+3
        print(function.__name__)
        return func
    return wrapper

@uppercase_decorator
def say_hi(a,b):
    return a+b
print(say_hi(4,3))

# ------------------------------
# def summa(c):
#     def summa1(*args, **kwargs):
#         func = c(*args,**kwargs)
#         u = sum(*args,**kwargs)
#         print (u)
#         return func
#     return summa1
# @summa

def say_hi(x):
    chetnoe = []
    nechotnoe = []
    for i in x:
        if i % 2 == 0:
            chetnoe.append(i)
        else:
            nechotnoe.append(i)
    return chetnoe, nechotnoe


chetnoe = []
nechotnoe = []
for i in range(100):
    if i % 2 == 0:
        chetnoe.append(i)
    else:
        nechotnoe.append(i)
print( chetnoe, nechotnoe)