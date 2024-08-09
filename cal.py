import streamlit as st

# Adds two numbers
def add(x, y):
    return x + y

# Subtracts two numbers
def subtract(x, y):
    return x - y

# Multiplies two numbers
def multiply(x, y):
    return x * y

# Divides two numbers
def divide(x, y):
    return x / y

def calculator():
    st.title("Mughisa Zulfiqar Calculator")

    num1 = st.number_input("Enter first number", value=0)
    operator = st.selectbox("Select operator", ("+", "-", "*", "/"))
    num2 = st.number_input("Enter second number", value=0)

    if st.button("Calculate"):
        try:
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                if num2 == 0:
                    st.error("Cannot divide by zero.")
                    return
                result = divide(num1, num2)
            st.success(f"Result: {result}")
        except ValueError:
            st.error("Invalid input. Please enter numeric values.")

if __name__ == "__main__":


    calculator()
