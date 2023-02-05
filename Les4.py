num = [100]
# for i in range(100):
#     print(i)
chetnoe = []
nechotnoe = []
for i in range(100):
    if i % 2==0:
        chetnoe.append(i)
    else:
        nechotnoe.append(i)

# print(chetnoe) 
# print(nechotnoe)


# for i in range(20):
#     if i>5 and i<10:
#         continue
#     print(i)

# name = 'Alymbek'
# age = "19"
# my_str = f"name: {name}, age: {age}"
# print(my_str)



a = [1,2,3,4,5,4,4,7,3,6,3,4,4,4,4,4]
# x = 0
summ = 0
# for i in a:
#     x = x+1
# print(x)

#  for i in a:
#     if i == 4:
#         x = x+1

for i in a:
    if i == 3 or i == 4:
        continue
    summ = summ+i

print(summ)




# a = 12



#     if a <=13 and a > 12:
#         print("qwerty")
#     elif a == 11 or a > 10:
#         print("ok")
#     elif != 36 and a <=11:
#         print("no")
#     elif != 13 and a>= 11:
#         print("No")
#     else:
#         print("Xaxa")



# список чисел, которые : 2, 3 делятся без остатка до 100

