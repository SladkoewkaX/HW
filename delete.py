# def filter_100_200(x):
#     a = []
#     for i in x:
#         if i >100 and i <120:
#             continue
#         else:
#             a.append(i)
#     return a
# list1 = [1,4,33,100,113,107,120,155,256]
# print(filter_100_200(list1))

# def filter_even(c):
#     a = []
#     for i in c:
#         if i % 2 == 0:
#             a.append(i)
#     return a
# list1 = [1,4,33,100,113,107,120,155,256]
# print(filter_even(list1))

# def num(x):
#     a = []
#     for i in range(min(x), max(x)): 
#         if i not in x: 
#             a.append(i)
#     return a
# list = [3,0,1]
# # list = [9,6,4,2,3,5,7,0,1]
# print(num(list))

def num(x):
    a = 0
    for i in x: 
        if i > a:
           a = i+1
    return a
list = [0,3,1,2]
print(num(list))

