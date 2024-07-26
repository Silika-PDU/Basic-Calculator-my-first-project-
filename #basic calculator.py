#basic calculator
#add, subract, multiply, divide

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divd(a, b):
    if b == 0:
        return "Error"
    else:
        return a / b 
    
#basic funtions defined 


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
#user input asked

print("add:", add(a, b))
print("subract:", sub(a, b)) 
print("multiply:", mult(a, b)) 
print("divide:", divd(a, b))
#main calculator