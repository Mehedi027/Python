from selenium.webdriver.common.devtools.v85.fetch import continue_request


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
def calculator():
    first_number = float(input("Type the first Number: "))
    old_output = first_number

    should_continue = True
    while should_continue:
        operation = input("Chose a Mathematical Operator: '+', '-', '*', '/'\n")
        second_number = float(input("Type the second number: "))

        if operation == "+":
            added_value = add(old_output, second_number)
            print(f"{old_output} {operation} {second_number} = {added_value}")
            old_output = added_value
        elif operation == "-":
            subtracted_value = subtract(old_output, second_number)
            print(f"{old_output} {operation} {second_number} = {subtracted_value}")
            old_output = subtracted_value
        elif operation == "*":
            multi_value  = multiply(old_output, second_number)
            print(f"{old_output} {operation} {second_number} = {multi_value}")
            old_output = multi_value
        elif operation == "/":
            divide_value = divide(old_output, second_number)
            print(f"{old_output} {operation} {second_number} = {divide_value}")
            old_output = divide_value
        restart = input(f"Type 'y' continue calculating with {old_output}, or type 'n' to start a new: \n")
        if restart == "n":
            should_continue = False
            calculator()

calculator()

#print(operators["*"](4,8))