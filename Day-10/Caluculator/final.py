# calculator 

import art
import os

# add
def add(n1, n2):
    return n1 + n2

# sub


def sub(n1, n2):
    return n1 - n2

# multiply


def mul(n1, n2):
    return n1 * n2

# Division


def div(n1, n2):
    return n1 / n2


# dict
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    print(art.logo)
    number1 = float(input("Enter the first number?: "))

    for i in operations:
        print(i)

    should_continue = True
    while should_continue:
        operation_symbols = input("Pick an operation : ")
        number2 = float(input("Enter the next number?: "))

        calculation = operations[operation_symbols]
        answer = calculation(number1, number2)

        print(f"{number1} {operation_symbols} {number2} = {answer} ")
        print("\n")

        if input(f"Type 'y' to continue calculating with {answer} , type 'n' to start a new caluculation : ") == "y":
            number1 = answer
        else:
            should_continue = False
            # Clearing the Screen
            os.system('cls')
            calculator()


calculator()
