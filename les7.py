# a = 3
# b = 5

# print(f"A is {a}, B is {b}")
# a,b = b,a 

# print(f"A is {a}, B is {b}")
# a,b = b,a 



# a = 3
# b = 5
# print(f"A is {a}, B is {b}")
# c = a
# a = b
# b = c

# print(f"A is {a}, B is {b}")
# a,b = b,a 




# my_list = [1,4,2,5,6,7,9,2,4,25,62]
# x = 0
# for i in my_list:
#     if i > x:
#         x = i
# print(x)

# my_list = [1,4,2,4,5,7,53,35,7,67,78,3]
# def x(c):
#     x = 0
#     for i in c:
#         if i > x:
#             x = i
#     return x

# print(x(my_list))

# my_list1= [1,4,2,4,5,7,53,35,7,67,78,3]
# def num(l):
#     x = 100
#     for i in l:
#         if i < x:
#             x = i
#     return x

# print(num(my_list1))

# : - slice



# my_list1= [1,4,2,4,5,7,53,35,7,67,78,3]
# print(sum(my_list1) / len(my_list1))

my_list1= [1,4,2,4,5,7,53,35,7,67,78,3]
def x(num):
    q = 0
    w = len(num) 
    e = 0 
    for i in num:
        q += i
    e = q / w 
    return e 
        
print(x(my_list1))
