
def plus(number1, number2):
    return number1+number2

def minus(number1, number2):
    return number1-number2
         
         
def div(number1, number2):    
    return number1/number2

def mult(number1, number2):
    return number1*number2

def calc():
    a = int(input("num1 : "))
    b = int(input("num2 : "))
    oper = input("oper : ")
    result = None 
    if oper == "+":
        result = a+b 
    elif oper == "-":
        result = a-b 
    elif oper == "*":
        result = a*b 
    elif oper == "/":
        result = a/b 
    else:
        result = "Error"
    return result 

print(calc())
