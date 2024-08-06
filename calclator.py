#  adds two numbers
def add(x, y):
    return x + y

#  subtracts two numbers
def subtract(x, y):
    return x - y

# multiplies two numbers
def multiply(x, y):
    return x * y


# divides two numbers
def divide(x, y):
    return x / y


def calculator():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = int(input("Enter second number: "))

            if operator == "+":
                result = add (num1, num2)
            elif operator == "-":
                result = subtract (num1, num2)
            elif operator == "*":
                result = multiply (num1, num2)
            elif operator == "/":
                result = divide  (num1, num2)
            else:
                print("Invalid operator")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

        # if quite print goodbye

        next_calculation = input("Do you wants to quit? (yes/no): ")
        if next_calculation == "yes":
            print('Good bye')
            break

    else:
        print("Invalid input")


calculator()