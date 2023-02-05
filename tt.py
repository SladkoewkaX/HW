# import math
# z = 600851475143
# def simply(x):
#     r = int(math.sqrt(x))
#     ls = []
#     for i in range(3,r):
#         if x%i == 0:
#             if simply(i) == []:
#                 ls.append(i)

#     return ls

# print(max(simply(z)))


# def num(x):
#     s = str(x)
#     a = int(s[::-1])
#     if a == x:
#         return True
#     else:
#         return False
# print(num(9009))

# def max_polindrom():
#     v = []
#     for i in range(100, 1000):
#         for j in range(100, 1000):
#             if num(i*j):
#                 v.append(i*j)
#     return v
# print(max(max_polindrom()))

        
        