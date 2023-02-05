a = int(input("Введите цифру :"))
num = [1,2,2,3,6,5,10]
def x(q):
    for i in range (len(q)):
        if a == num[i]:
            return i 
        elif i == len(q)-1:
            num.append(a)
            print(num)
            return len(q)-1
print(x(num))