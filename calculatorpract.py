def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/b


a = input("Please enter your first number.\n")
b = input("Please enter your second number. \n")
operator = input("Would you like to add, subtract or divide? enter +, -, /, *")

if operator == "+":
   add(a,b)
else:
    print("oh no")

