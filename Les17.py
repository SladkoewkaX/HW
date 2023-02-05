# def get_people(people_id, value):
#     peoples = [{'name': 'Bapaev', 'address': 'PSC 2840, Box 4433\nAPO AE 82541', 'email': 'brenda90@yahoo.com'}, {'name': 'Tracie Peters', 'address': '97361 Flynn Drive\nNorth Candice, HI 51876', 'email': 'jane26@robertson.com'}, {'name': 'Donald Adams', 'address': '5915 Geoffrey Motorway Apt. 669\nNorth Jason, AK 27894', 'email': 'mark29@woods-cooley.biz'}, {'name': 'Miranda Martin', 'address': '84439 Alyssa Wells\nPort Alexander, MS 97050', 'email': 'natasha62@gmail.com'}, {'name': 'Mark Dickerson III', 'address': '91298 Ashley Mission\nHarveymouth, MA 12655', 'email': 'lcunningham@gmail.com'}]
#     for i in peoples:
#         print(i['name'])
#         print(i['address'])
#         print(i['email'])
#     if people_id > len(peoples):
#         return 'error'
#     return peoples[people_id-1][value]
# print(get_people(1,'name'))


# class friend:
#     def __init__(self, name, work , age):
#         self.name = name
#         self.work = work
#         self.age = age

# Danil = friend('Danil','on Factory' , 19 )
# print(Danil.name)
# print(Danil.work)
# print(Danil.age)


class Animal:
    live = True
class Dog(Animal):
    mammal = True
    def __init__(self, nickname, breed, age):
        self.breed = breed
        self.nickname = nickname
        self.age = age
    @property
    def get_info(self):
        return f'name: {self.nickname}, age: {self.age}, breed: {self.breed}'
    def age_plus(self):
        self.age = self.age+1

chapi = Dog('Chapi', "Haski", 10)
chapi.age_plus()
print(chapi.live)
print(chapi.get_info)
# print(chapi.get_info())



# class friend:
#     def __init__(self, name, surname , exp, paycheck):
#         self.name = name
#         self.surname = surname
#         self.exp = exp
#         self.paycheck = paycheck
#     def payment(self, m):
#         self.paycheck = self.paycheck+m
#     def exp_1(self, e):
#         self.exp = self.exp+e

#     def about(self):
#         return f'name: {self.name}, surname: {self.surname}, exp: {self.exp}, : paychek: {self.paycheck} '
# Nurslan = friend("Nurslan", "Abibekob", 2 , 8000)
# Nurslan.payment(0)
# Nurslan.exp_1(0)
# print(Nurslan.about())