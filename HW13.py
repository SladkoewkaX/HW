# a = [12,65,324,23,35]
# def med(x):
#     res = 0
#     mediana = 0
#     x.sort()
#     if len(x) % 2 == 0:     
#         mediana = int((len(x)))# находим середину 
#         res = (x[mediana]) + (x[mediana])/2 # находим результат
#         return res
#     else: #если не четное
#         mediana = int(len(x)/2)
#         return x[mediana]
# print(med(a))


# a = [12,65,324,23,35]
# a.sort()
# b= len(a)
# assert b % 2 != 0
# print(a[b // 2])


# from statistics import median

# print(median([12,65,324,23,35]))

def median(lst):
    sortedLst = sorted(lst)
    len_l = len(sortedLst)
    index = (len_l-1)//2
    if (len_l % 2 == 0):
        return (sortedLst[index] + sortedLst[index+1])//2
    else:
        return sortedLst[index]
print(median([1,3,5,9]))