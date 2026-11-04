def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
if b == 0:
    raise ValueError("Cannot divide by zero.")
return a / b

def get_number(prompt):
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print("That is not a valid number. Please try again")

def get_operation():
    operations = {"+", "-", "*", "/"}
    while True:
        choice = input("Choose an operation (+, -, *, /): ").strip()
        if choice in operations:
            return choice
        print("Invalid operation. Please enter +, -, * or /.")

def calculate(a, operation, b):
    if operation == "+":
        return add(a, b)
    if operation == "-":
        return substract(a, b)
    if operation == "*":
        return multiply(a, b)
    if operation == "/":
        return divide(a, b)

def interface():
    print("== Calculator ==")
    while True:
        a = get_number("Enter the first number: ")
        operation = get_operation()
        b = get_number("Enter the second number: ")
    try:
        result = calculate(a, operation, b)
        print(f"Result: {a} {operation} {b} = {result}")
    except ValueError as error:
        print(f"Error: {error}")
    again = input("Calculate again? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break

if __name__ == "__main__":
    main()
