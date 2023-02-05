# Для вычисления суммы до 6 факториала

# a = int(input("Введите факториал: "))
# def x(q):
#     factor = 1
#     for i in range(2, q+1):
#         factor *= i
#         num1 = factor % 10
#         num2 = factor % 100 // 10
#         num3 = factor // 100
#         num4 = factor //10000
#     print("Сумма факториала равна:", num1 + num2 + num3 + num4)
#     return factor
# print(x(a))



# Для вычисления суммы факториала 7
# a = int(input("Введите факториал: "))
# def x(q):
#     factor = 1
#     for i in range(1, q+1):
#         factor *= i
#         num1 = factor % 10
#         num2 = factor % 100 // 10
#         num3 = factor // 1000
#         num4 = factor //10000
#     print("Сумма факториала равна:", num1 + num2 + num3 + num4)
#     return factor
# print(x(a))


def fact(num):
    a = 1
    b = []
    c = 0
    for i in range(2,num+1):
        a *= i
    for i in str(a):
        c += int(i)
    return c
print(fact(7))