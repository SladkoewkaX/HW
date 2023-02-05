# import random

# def tree(x):
#     for i in range(1, x, 2):
#         t = (x-i) // 2 * ' '
#         print(t + '*' * i) 
#     for i in range(0,2):
#         print('         | |          ')
# print(tree(22))


# def critmas_tree(n):
#     a = ' '
#     b = '*'
#     count = 1
#     last = n*2-1
#     r = ''
#     for i in range(n):
#         c = b*count
#         if i == 0:
#             c ='🌟'
#         g = (last-len(c))//2
#         r = r+a*g+f'{c}'+a*g+'\n'
#         count = count +2
#     return r

# print(critmas_tree(10))


