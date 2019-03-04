first = input("Type in your first number:\n")
second = input("Type in your second number:\n")
operator = input("Please choose an operator to perform math:::  +, - , * , or /\n")


def add_number():
    third = (int(first) + int(second))
    print(third)

def subtract_number():
    third = (int(first) - int(second))
    print(third)

def multiply_number():
    third = (int(first) * int(second))
    print(third)

def divide_number():
    third = (int(first) / int(second))
    print(third)


if operator == "+":
    add_number()

elif operator == "-":
    subtract_number()

elif operator == "*":
    multiply_number()

elif operator == "/":
    divide_number()

else:
    print("oh no")
