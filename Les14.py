# def slova(x):
#     a = ''
#     for i in x:
#         a = a+(letter[i])
#     return a 
# letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# l1 = [18,12,15,2,0]
# print(slova(l1))


# def slova(x):
#     letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     return "".join([letter[i] for i in x])
# print(slova( [18,12,15,2,0]))



#-------------------------------------------------



def slova(x):
    letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    n = 0 

    for i in x:
        n = n+letter.index(i)+1
    return n 
print(slova('привет'))





























# a = int(input("Введите индекс буквы: "))
# letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# def slova(x):
#     for i in range(len(x)):
#         if a == letter[i]:
#             return i
#         elif i == len(x)-1:
#             print(letter)
#             return len(x)-1
# print(slova(a))