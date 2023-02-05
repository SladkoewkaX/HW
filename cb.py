from calendar import c
import random
def random_num(c):
    x = [random.randint(0,9) for i in range(c)]
    print('Загаданное число: ' + str(x))
    count = -1
    while True:
        count += 1
        print("Отгадал " + str(count))
        a = [int(i) for i in str(input('Введите число: '))]
        cow = 0
        bull = 0
        if a == x:
            print("Ты выйграл", "на это ушло " +str(count)+ ' попыток.')
        else:
            for j in range(0, c):
                if a[j] == x[j]:
                    cow += 1
                elif a[j] in x:
                    bull += 1
        print('Коров: ' + str(cow)+ " Быков: " + str(bull))
print(random_num(c))
