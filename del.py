import re

def start_num(x):
    if int(x) == [4,5,6]:
        return True
    return False

def four_num(x):
    if '-' in x:
        split_num = x.split('-')
    else:
        split_num = re.findall('....', x)
    for i in split_num:
        if len(i) > 4:
            return False
    return True

def num_repeat(x):
    x = x.replace('-','')
    count = 1
    lenght = []
    for i in range(1, len(x)):
        if x[i-1] == x[i]:
            count +=1
        else:
            lenght.append[(x[i-1], count)]
            count = 1
    lenght.append[(x[i], count)]
    for i in lenght:
        if i[1] >=4:
            return False
    return True

def all_def(x):
    if num_repeat(x) == False or four_num(x)== False or start_num(x) == False:
        return "Invalid"
    return 'Valid'






print(all_def(4123456789123456))
print(all_def(5123-4567-8912-3456))
print(all_def(61234-567-8912-3456))
print(all_def(4123356789123456))
print(all_def(5133-3367-8912-3456))
print(all_def(5123 - 3567 - 8912 - 3456))
   