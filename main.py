#Defining functions
def add(a, b):
    result = a + b
    print(result)

def sub(a, b):
    result = a - b
    print(result)

def mul(a, b):
    result = a * b
    print(result)
    
def div(a, b):
    result = a / b
    print(result)

#Main Loop
while True:
    print("A:Addition")
    print("B:Substraction")
    print("C:Multiplication")
    print("D:Division")
    print("E:Exit")
    choice = input().lower()
    #If Statements
    if choice == "a":
        first_number = int(input("What is the first number"))
        second_number = int(input("What is the second number"))
        add(first_number, second_number)
    elif choice == "b":
        first_number = int(input("What is the first number"))
        second_number = int(input("What is the second number"))
        sub(first_number, second_number)

    elif choice == "c":
        first_number = int(input("What is the first number"))
        second_number = int(input("What is the second number"))
        mul(first_number, second_number)

    elif choice == "d":
        first_number = int(input("What is the first number"))
        second_number = int(input("What is the second number"))
        div(first_number, second_number)

    elif choice == "e":
        break
print("Bye!") 