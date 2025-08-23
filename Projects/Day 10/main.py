# Calculator
import os
def clear():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')
logo = """
 _____________________
|  _________________  |
| |  FalconXAsmit   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("Enter your first number: "))

    while should_accumulate:
        for symbols in operations:
            print(symbols)
        operation_symbol = input("What operation do you want to apply: ")
        num2 = float(input("Enter the next number: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculations with {answer}, type 'n' to start a new calculation, type 'q' to quit: ").lower()
        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            should_accumulate = False
            clear()
            calculator()
        else:
            print("Goodbye")

calculator()
