# Есть лист 
# my_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
# Используя цикл for прибавьте к каждому значению листа единицу и добавьте получившееся значение в лист my_list2 . 
# В итоге у вас должно получится my_list2 = [ 2, 3, 4 ,5 , 6, 7 , 8 , 9 , 10 ]
# Скиньте код , который вы напишите

# my_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
# add = 1
# my_list2 = []

# for i in my_list:
#     add = add + 1
#     my_list2.append(add)

# print(my_list2)    

import random
import string


# def generate_alphanum_random_string(length):
#     letters_and_digits = string.ascii_letters + string.digits
#     rand_string = ''.join(random.sample(letters_and_digits, length))
#     print("Alphanum Random string of length", length, "is:", rand_string)


# print(generate_alphanum_random_string(16))

# password = ''.join(random.choice(string.ascii_letters) for i in range(8))
# print("Random password is:", password)


characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for i in range(8))
print("Random password is:", password)