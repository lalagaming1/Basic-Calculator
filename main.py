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
    choice = input("""A:Multiplication
    B:Substraction
    C:Multiplication
    D:Division
    E:Exit""")
    