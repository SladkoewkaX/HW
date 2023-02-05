
# my_list = []
# for i in range(1, 101):
#     if i % 2==0 and i % 3 == 0:
#         my_list.append(i)
# print(my_list)

# my_list = []
# for i in range(1, 92):
#     if i % 2==0:
#         my_list.append(i)
# print(len(my_list))
# print(my_list)

# my_list = []
# for i in range(1, 100):
#     if i % 2==0:
#         my_list.append(i)
#     elif len(my_list) == 45:
#         break
# print(len(my_list))
# print(my_list)

# for i in range(20):
#     if i>5 and i<10:
#         continue
# print(i)

# a = int(input())
# v = (a ** 3)
# s = (6 * a ** 2)
# print(f"Объем = {v}")
# print(f"Площадь полной поверхности = {s}")

# a = int(input())
# b = int(input())
# func = 3*(a + b)**3 + 275*b**2 - 127*a - 41
# print(func)

# a = int(input())
# b = a + 1
# c = a - 1
# print(f"Следующее за числом {a} число: {b}")
# print(f"Для числа {a} предыдущее число: {c}")

# a = int(input())
# print(f"Следующее за числом {a} число: {a + 1} \nДля числа {a} предыдущее число: {a - 1}")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print((a + b + c + d) * 3 )

# print((sum((int(input()) for i in range(4))) * 3))

# a = int(input())
# b = int(input())
# print(a + b, a - b, a * b, sep='\n' )

# a = int(input())
# b = int(input())
# print(f"{a} + {b} = {a + b}", f"{a} - {b} = {a - b}", f"{a} * {b} = {a * b} ", sep='\n')

# a, b = int(input()), int(input())
# print(a, '+', b, '=', a + b , a, '-', b, '=', a - b, )
# print(a, '-', b, '=', a - b)7

# print(a, '*', b, '=', a * b)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a + b*(c-1))

# a = int(input())
# print(a, a * 2, a * 3, a * 4, a * 5, sep="---")

# a = int(input())
# for i in range(9):
#     if i == 5:
#         print(a * i)
#     else:
#         print(a * i, end='---')
#     i += 1



# a = int(input())
# print((a + 3) // 4)

# a = int(input())
# c = 1
# b = 20
# if a // 60:
#     print(c+1)
# print(f"{a} мин - это {c} час {b} минут.")

# a = int(input())
# h = a // 60
# m = a % 60
# print(f"{a} мин - это {h} час {m} минут.")

# a = 135
# h = a // 60
# m = a % 60
# print(h)
# print(m)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Искомое число =', last_digit * 10 + first_digit)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# summ = digit1 + digit2 + digit3
# summ2 = digit1 * digit2 * digit3
# print(f"Сумма цифр = {summ}")
# print(f"Произведение цифр = {summ2}")

# num = int(input())
# n3 = num % 10
# n2 = (num // 10) % 10
# n1 = num // 100
# n1 , n2 , n3 = str(n1), str(n2),str(n3)
# reverse1 = n1 + n3 + n2
# reverse2 = n2 + n1 + n3
# reverse3 = n2 + n3 + n1
# reverse4 = n3 + n1 + n2
# reverse5 = n3 + n2 + n1
# print(num, reverse1 , reverse2, reverse3, reverse4,reverse5, sep = '\n')

# a,b,c = input()
# print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')

# num = int(input())
# a = num % 10 #4 number
# b = (num // 10) % 10 # get three number
# c = (num // 100) % 10 # get two number
# d = num // 1000 # get first number
# print(f"Цифра в позиции тысяч равна {d}")
# print(f"Цифра в позиции сотен равна {c}")
# print(f"Цифра в позиции десятков равна {b}")
# print(f"Цифра в позиции единиц равна {a}")

# a = 17 * '*'
# b = "*" 
# c = " "
# d =  17 * '*'
# print(a)
# print(b, c * 14 + '*')
# print(b, c * 14 + '*')
# print(d)

# print('*' * 17)
# print('*', '*', sep=' ' * 15)
# print('*', '*', sep=' ' * 15)
# print('*' * 17)

# a = int(input())
# b = int(input())
# sq = (a+b)**2
# sum = a**2 + b**2
# print(f"Квадрат суммы {a} и {b} равен {sq}")
# print('Сумма квадратов', a, 'и', b, 'равна', sum)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# sum = (a**b) + (c**d)
# print(sum)


# a = int(input())
# sum = a * 1
# sum2 = a * 10 + a
# sum3 = a * 100+ sum2
# print(sum + sum2 + sum3)

# n = input()
# print(int(n) + int(n * 2) + int(n * 3))

# a = input()
# b = input()
# if a == b:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# a = int(input())
# if a % 2 == 0 :
#     print("Четное")
# else:
#     print("Нечетное")

# a = int(input())
# f = a % 10
# l = a // 1000
# sum = f + l
# s = (a // 100) % 10
# t = (a // 10) % 10
# summ = s - t
# if sum == summ:
#     print("ДА")
# else:
#     print("НЕТ")

# a = int(input())
# if a < 18:
#     print("Доступ запрещен")
# else:
#     print("Доступ разрешен")

# a, b, c = int(input()), int(input()), int(input())
# if a == a and a > a+1 and a > + 2:
#     print("YES")
# else:
#     print("NO")

# a, b, c = int(input()), int(input()), int(input())
# if b - a == c - b:
#     print("YES")
# else:
#     print("NO")

# a, b, = int(input()), int(input())
# if a > b:
#     print(b)
# else:
#     print(a)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a > b:
#     a = b

# if c > d:
#     c = d

# if a > c:
#     a = c

# print(a)


# a = int(input())
# if a <= 13:
#     print("детство")
# elif a >= 14 and a < 24:
#     print("молодость")
# elif a <= 59:
#     print("зрелость")
# elif a > 60:
#     print("старость")

# a, b, c = int(input()), int(input()), int(input())
# sum = 0
# if a > 0:
#     sum += a
# if b > 0:
#     sum += b
# if c > 0:
#     sum += c
# print(sum)
