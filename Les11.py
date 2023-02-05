# a = '6'
# try:
#     int(a)
#     print(a)
# except ValueError:
#     print("Букву нельзя превратить в число")



# list_num = 'qq13d3d1d13d13'
# def x(q):
#     num = []
#     for i in list_num:
#         try:
#             num.append(int(i))
#         except ValueError:
#             continue
#     return num
# print(x(list_num))



# def x(n):
#     fibs = [1, 2]
#     fib1 = 1
#     fib2 = 2
#     for i in range(n-2):
#         fibsum = fib1+fib2
#         fibs.append(fibsum)
#         fib1 = fib2
#         fib2 = fibsum
#     return fibs

# print(x(7))



# a = input("Введите число: ")
# def x(c):
#     c = a[::-1]
#     return c
# print(x(a))

# a = 1500
# b = ""
# a = str(a)
# for i in range(len(a),0,-1):
#     b += a[i-1]
# print(b)
