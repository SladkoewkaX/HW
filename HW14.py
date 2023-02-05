# У вас есть лист с предыдущего урока урока,который хранит словари с данными . 
# Создайте функцию , которая принимает индекс и название поля . Ваша функция должна вернуть поле из словаря по индексу

def get_people(people_id, value):
    peoples = [{'name': 'Matthew Evans', 'address': 'PSC 2840, Box 4433\nAPO AE 82541', 'email': 'brenda90@yahoo.com'}, {'name': 'Tracie Peters', 'address': '97361 Flynn Drive\nNorth Candice, HI 51876', 'email': 'jane26@robertson.com'}, {'name': 'Donald Adams', 'address': '5915 Geoffrey Motorway Apt. 669\nNorth Jason, AK 27894', 'email': 'mark29@woods-cooley.biz'}, {'name': 'Miranda Martin', 'address': '84439 Alyssa Wells\nPort Alexander, MS 97050', 'email': 'natasha62@gmail.com'}, {'name': 'Mark Dickerson III', 'address': '91298 Ashley Mission\nHarveymouth, MA 12655', 'email': 'lcunningham@gmail.com'}]
    if people_id > len(peoples):
        return 'error'
    return peoples[people_id-1][value]
print(get_people(1,'name'))