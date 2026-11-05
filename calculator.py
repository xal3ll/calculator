def calc() -> int:
    print("=== Calculator ===")
    number = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    number2 = float(input("Enter the second number: "))
    result = 0
    if operation == "+":
        result = number + number2
    elif operation == "-":
        result = number - number2
    elif operation == "*":
        result = number * number2
    elif operation == "/":
        if number2 == 0:
            print("Error: Cannot divide by 0")
            return
        result = number / number2
    else:
        print("Invalid operation.")
        return
    print(f" {number} {operation} {number2} = {result}")


calc()



def hello():
    print("hello")

hello()
