Txt = set()

from random import randint
mtx = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

mtx[randint(0, 24)][randint(0, 17)] = 'З'
for x in range(25):
    for y in range(18):
        if mtx[x][y] == 'З':
            Txt.add(mtx[x][y])
            break
    if len(Txt) > 0:
        break
        

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def rec(i):
    if alphabet.lower()[i] != 'д':
        rec(randint(0, 32))
    else:
        Txt.add(alphabet.lower()[i])
    
    
rec(10)

from math import pi
from decimal import Decimal as dec
Mp = dec(pi)
Np = dec(Mp * ord('р'))

Txt.add(chr(Np / Mp))

Txt.add(chr((((1072 >> 1) - 1) >> 1 ^ 12 ^ 122 ^ 134 | 512) ^ 1995))

t = '''авдон мадон Водон ропон.
       запон ливон амрон ферон
       а также фреон, антон и 
       барон'''

t = ''.join([i.strip(alphabet.lower() + '., ') for i in t])
Txt.add(list(t)[0].lower())

class C:
    def __init__(self, name):
        if 'с' in name:
            self.__name = name
        else:
            raise TypeError('There is must be letter "c"')
        
    @property
    def name(self):
        return self.__name[self.__name.find('с')]

Object1 = C('Алиса')
Txt.add(Object1.name)

т = lambda x: True if all(i > 10 for i in range(12)) else 'т'
Txt.add(т(282))

from string import ascii_letters as буквы
Txt.add(буквы[1].upper())

roster = [randint(1, 100) for _ in range(12)]
for i in range(len(roster)):
    for j in range(len(roster)):
        if roster[i] < roster[j]:
            roster[i], roster[j] = roster[j], roster[i]
            
if roster == sorted(roster): Txt.add('у')
    
def f(a):
    def f1(b):
        def f2(c):
            return a + b + c
        return f2
    return f1

Txt.add((chr(f(1)(512)(568))))

#with open('C:/Users/User/Desktop/123.txt', 'r', encoding='utf-8') as File:
#    Txt.add(File.readline())
# :(
Txt.add(' ')

# P.S Кажется, вы сюда ещё вернётесь...
class Chess:
    chessboard = [['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.']]
    
    for i in ('Q', 'B', 'K'):
        chessboard[randint(0, 7)][randint(0, 7)] = i 
            
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.qp = None
        self.bp = None
        self.kp = None
        
    def knight_move(self):
        t = True
        for i in range(len(self.chessboard)):
            if t == False: break
            for j in range(len(self.chessboard)):
                if self.chessboard[i][j] == 'K':
                    self.kp = (i, j)
                    t = not(t)
                    break
        return abs(self.x - self.kp[0]) == 2 and abs(self.y - self.kp[1]) == 1 or abs(self.x - self.kp[0]) == 1 and abs(self.y - self.kp[1]) == 2
    
    def bishop_move(self):
        t = True
        for i in range(len(self.chessboard)):
            if t == False: break
            for j in range(len(self.chessboard)):
                if self.chessboard[i][j] == 'B':
                    self.bp = (i, j)
                    t = not(t)
                    break
        return abs(self.x - self.bp[0]) == abs(self.y - self.bp[1]) 
    
    def queen_move(self):
        t = True
        for i in range(len(self.chessboard)):
            if t == False: break
            for j in range(len(self.chessboard)):
                if self.chessboard[i][j] == 'Q':
                    self.qp = (i, j)
                    t = not(t)
                    break
        return abs(self.x - self.qp[0]) == (abs(self.y - self.qp[1])) or self.x == self.qp[0] or self.y == self.qp[1]        
                    
    def lucky_chance(self):
        while self.queen_move() != True and self.bishop_move() != True and self.knight_move() != True:
            self.chessboard = [['.', '.', '.', '.', '.', '.', '.', '.'],
                               ['.', '.', '.', '.', '.', '.', '.', '.'],
                               ['.', '.', '.', '.', '.', '.', '.', '.'],
                               ['.', '.', '.', '.', '.', '.', '.', '.'],
                               ['.', '.', '.', '.', '.', '.', '.', '.'],
                               ['.', '.', '.', '.', '.', '.', '.', '.'],
                               ['.', '.', '.', '.', '.', '.', '.', '.'],
                               ['.', '.', '.', '.', '.', '.', '.', '.']]
            
            for i in ('Q', 'B', 'K'):
                self.chessboard[randint(0, 7)][randint(0, 7)] = i
        return 'м' 
    
    
board1 = Chess(4, 4)
Txt.add(board1.lucky_chance())

if bool('У меня слишком много свободного времени. У тебя, кстати, тоже.') == True:
    Txt.add('и')

d1 = [i for i in range(10, 20)]
d2 = [i ** 2 for i in range(10, 20)]
d3 = dict(zip(d1, d2))
t = d3.setdefault(441, 'p')
Txt.add(t)

from math import factorial as fuck
def brain(n):
    for i in range(25):
        t = n
        for j in range(1, i):
            for o in range(j, 0, -1):
                t //= o
                if fuck(t) == n:
                    return f'{t} !'
            t = n
            
if int(brain(720).split()[0]) == 6:
    Txt.add(brain(1).split()[1])
    
Txt = list(Txt)
Txt[Txt.index('B')] = 'В'
Txt[Txt.index('p')] = 'р'
Txt.append(',')

'''
Diction = dict(zip(range(16), Txt))
t1 = list(Diction.values())[:2]
t2 = list(Diction.values())[2:4]
t3 = list(Diction.values())[4:6]
t4 = list(Diction.values())[6:8]
t5 = list(Diction.values())[8:10]
t6 = list(Diction.values())[10:12]
t7 = list(Diction.values())[12:14]
t8 = list(Diction.values())[14:16]
while ''.join(t1) != 'Зд':
    shuffle(t1)
    
while ''.join(t2) != 'ра':
    shuffle(t2)
    
while ''.join(t3) != 'вс':
    shuffle(t3)
    
while ''.join(t4) != 'тв':
    shuffle(t4)

while ''.join(t5) != 'уй':
    shuffle(t5)
    
while ''.join(t6) != ' ,':
    shuffle(t6)
    
while ''.join(t7) != 'ми':
    shuffle(t7)
    
while ''.join(t8) != 'р!':
    shuffle(t8)
    
print(''.join(t1) + ''.join(t2) + ''.join(t3) + ''.join(t4) + ''.join(t5) + ''.join(t6) + ''.join(t7) + ''.join(t8), sep='')
...'''
print('Здравствуй, мир!')  