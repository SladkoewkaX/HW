def copy(x):
    res = []
    for i in x:
        if i not in res:
            res.append(i)
    return res
a = [1,2,2,4,8,5,7,4,1,7]
print(copy(a))