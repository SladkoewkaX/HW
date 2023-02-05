def num1(*lol):
    a=[]
    for i in lol:
        if i%2 == 0:
            a.append(i)
    print(a)
    return a
num1(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)


# def num1(lol):
#     a=[]
#     for i in range(lol):
#         if i%2 == 0:
#             a.append(i)
#     return a
# a = num1(22)
# print(a)
