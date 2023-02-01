#Defining functions
def add(a, b):
    result = a + b
    return(result)

def sub(a, b):
    result = a - b
    return(result)

def mul(a, b):
    result = a * b
    return(result)
    
def div(a, b):
    result = a / b
    return(result)

#Main Loop
while True:
    print("A:Addition")
    print("B:Substraction")
    print("C:Multiplication")
    print("D:DIvision")
    print("E:Exit")
    choice = input()