# Basic calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def power(a, b):
    return a ** b

# Function to get valid number input from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Function to get valid operation from the user
def get_operation():
    while True:
        operation = input("Enter the operation (+, -, *, /, ^): ")
        if operation in ['+', '-', '*', '/', '^']:
            return operation
        else:
            print("Invalid operation! Please choose one of +, -, *, /, or ^.")

# Main calculator function
def calculator():
    print("Welcome to the Basic Calculator!")
    while True:
        print("\nMenu:")
        print("1. Perform a calculation")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ")
        
        if choice == '2':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice == '1':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            operation = get_operation()
            
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '^':
                result = power(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid choice! Please select 1 or 2.")

# Start the calculator
if __name__ == "__main__":
    calculator()
