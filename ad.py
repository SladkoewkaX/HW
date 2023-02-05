# a = [{'id':0, 'slug': 'mrslotty', 'name':'MrSlotty'},
# {'id':1, 'slug':"truelab", 'name': 'TrueLab'},
# {'id':2, 'slug':'platipus', 'name': 'Platipus'},
# {'id':3, 'slug':'b1gaming',  'name':'BGaming'},
# {'id':4, 'slug':'belatra',  'name':'Belatra'},
# {'id':5, 'slug':'mascot', 'name': 'Mascot'},
# {'id':6, 'slug':'gamshy', 'name': 'Gamshy'},
# {'id':7, 'slug':'sapadgaming', 'name': 'Spadegaming'},
# {'id':8, 'slug':'wazdan',  'name':'Wazdan'}]

# def task(x):
#     return list((f"{i['id']}, {i['name']} Trial ({i['slug']})" for i in x))
# print(task(a))

# a = [{'id':0, 'slug': 'mrslotty', 'name':'MrSlotty'},
# {'id':1, 'slug':"truelab", 'name': 'TrueLab'},
# {'id':2, 'slug':'platipus', 'name': 'Platipus'},
# {'id':3, 'slug':'b1gaming',  'name':'BGaming'},
# {'id':4, 'slug':'belatra',  'name':'Belatra'},
# {'id':5, 'slug':'mascot', 'name': 'Mascot'},
# {'id':6, 'slug':'gamshy', 'name': 'Gamshy'},
# {'id':7, 'slug':'sapadgaming', 'name': 'Spadegaming'},
# {'id':8, 'slug':'wazdan',  'name':'Wazdan'}]

# def task(x):
#     return list(map((lambda i:(i['id'],f"{i['name']} Trial ({i['slug']})")), x))
# print(task(a))


# from datetime import date

# def time(x,c,v):
#     try:
#         date(x,c,v)
#         return True
#     except:
#         return False
# print(time(2021,10,32))


# def shift(list, step):
#     if step < 0:
#         step = abs(step)
#         for i in range(step):
#             list.append(list.pop(0))
#     else:
#         for i in range(step):
#             list.insert(0, list.pop())
# a = [1,2,3,4,5,6,7]

# # shift(a,3)
# # print(a)

# shift(a,-3)
# print(a)

# import re
# # result = re.match(r'AV', 'AV Analytics Vidhya AV')
# # print(result)


# match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
# print(match.group(1))


print(30*25)
