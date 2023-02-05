class Wallet:
    def __init__(self, plus, minus, percentadd, percentfromminus):
        self.plus = plus
        self.minus = minus
        self.percentadd = percentadd
        self.percentfromminus = percentfromminus
    
    def plus1(self, p):
        self.plus = self.plus + p
    
    def minus1(self, m):
        self.minus = self.minus - m
    
    def percentfromminus1(self, i):
         self.percentfromminus = self.minus / 100 * i
    
    def percentadd1(self, x):
        self.percentadd = self.percentadd * (1 + x / 100)
    
    def all(self):
        return f'plus: {self.plus}, minus: {self.minus},percentfromminus: {self.percentfromminus}, percentadd: {self.percentadd}'     

wallet1 = Wallet(900, 800, 700, 0 ) 
wallet1.plus1(200)
wallet1.minus1(400)
wallet1.percentfromminus1(5)
wallet1.percentadd1(30) 
print(wallet1.all())









# class wallet:
#     def __init__(self,balance):
#         self.balance = balance
        
#     @property
#     def info(self):
#         return f"Баланс вашего кошелька:{self.balance}"
 
#     def plus(self,num2):
#         self.balance=self.balance+num2
#         return self.balance
 
#     def minus(self,num1):
#         self.balance=self.balance-num1-(num1/100*1)
#         return self.balance
 
#     def persent(self,persent):
#         self.balance=self.balance+(self.balance/100*persent)
#         return self.balance
 
# my_wallet = wallet(float(input("Введите баланс вашего кошелка:")))
# my_wallet.plus(float(input("Введите сумму прибавления баланса:")))
# my_wallet.persent(float(input("Введите процент добавления вашего кошелька(%):")))
# my_wallet.minus(float(input("Введите сумму списания баланса(с баланса будет списан процент от суммы списания):")))
 
# print(my_wallet.info)






# class Wallet:
#     def __init__(self,owner,cash,minus,pluss,penalty_fee,per):
#         self.owner=owner
#         self.cash=cash
#         self.pluss=pluss
#         self.minus=minus
#         self.penalty_fee=penalty_fee
#         self.per=per
 
#     def get_info(self):
#         return f'Owner:{self.owner}\nCash:{self.cash}\nPluss:{self.pluss}\nMinus:{self.minus}\nPenalty_fee:{self.penalty_fee}\nPer:{self.per}'
 
#     def pluss_plus(self,pluss):
#         self.pluss= self.cash+pluss
 
#     def minus_plus(self,minus):
#         self.minus= self.cash-minus
 
#     def penalty_fee_plus(self):
#         self.penalty_fee=(self.cash-self.minus)*0.01
 
# #Какое число соответствует 35 % от числа 1000 ?
#     def per_plus(self,per):
#         self.per= self.cash/100*per
 
# #Сколько процентов составляет 35 от числа 1000 ? 
#     def per_plus(self,per):
#         self.per= 100/(self.cash/per)
 
# #Прибавить 35% к числу 1000
#     def per_plus(self,per):
#         self.per= self.cash/100*per+self.cash
 
 
# # Вычесть 35% из числа 1000
#     def per_plus(self,per):
#         self.per= self.cash-(self.cash/100*per)
 
 
# money = Wallet('Zhiba',1000,0,0,0,0)
# money.minus_plus(400)
# money.pluss_plus(200)
# money.penalty_fee_plus()
# money.per_plus(35)
# print(money.get_info())