def r():
    d = 5
    v = 6
    return [[i * j for j in range(v)] for i in range(d)]

a = r()

for i in a:
    for j in i:
        print(j, end=' ')
    print()
