a = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def chisla(x):
    my_list = []
    for num in x:
        for i in range(2, num):
            if num % i == 0:
                break
            elif num not in my_list:
                my_list.append(num)
    return my_list
print(chisla(a))



# # Работает, но без списка
# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# def chisla(x):
#     spisok = []
#     for i in range(2,x):
#         if x % i == 0:
#             spisok.append(i)
#             return False
#     return True
# for number1 in a:
#     if chisla(number1):
#         print(number1)