# calculator
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

number1 = int(input("Enter the first number?: "))


for i in operations:
    print(i)

operation_symbols = input("Pick an operation from the line above: ")
number2 = int(input("Enter the second number?: "))

calculation = operations[operation_symbols]
first_answer = calculation(number1, number2)

print(f"{number1} {operation_symbols} {number2} = {first_answer} ")

operation_symbols = input("Pick an operation : ")
number3 = int(input("Enter the next number?: "))

calculation = operations[operation_symbols]
second_answer = calculation(first_answer, number3)
print("/n")

print(f"{first_answer} {operation_symbols} {number3} = {second_answer} ")
