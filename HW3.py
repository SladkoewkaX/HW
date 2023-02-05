# my_list = []
# for i in range(1, 100):
#     if i % 2==0:
#         my_list.append(i)
#     elif len(my_list) == 45:
#         break
# print(len(my_list))
# print(my_list)


# Ver 2.0 через старт,стоп и степ
my_list = []
for i in range(5):
    if i % 2==0:
        my_list.append(i)
        continue
print(my_list)

# my_list = []
# for i in range(float(0, 45, 2)):
#     my_list.append(i)
# print(my_list)

# def num1(*lol):
#     a=[]
#     for i in lol:
#         if i%2 == 0:
#             a.append(i)
#     print(a)
#     return a
# num1(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
