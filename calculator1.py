import math

# Calculation history list
history = []

# Basic operations
def add(a, b):
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    history.append(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    result = a / b
    history.append(f"{a} / {b} = {result}")
    return result

def modulo(a, b):
    result = a % b
    history.append(f"{a} % {b} = {result}")
    return result

def power(a, b):
    result = a ** b
    history.append(f"{a} ^ {b} = {result}")
    return result

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number"
    result = math.sqrt(a)
    history.append(f"√{a} = {result}")
    return result

# Input handling
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Power")
    print("7. Square Root")
    print("8. Show History")
    print("9. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            operations = {
                "1": add,
                "2": subtract,
                "3": multiply,
                "4": divide,
                "5": modulo,
                "6": power
            }
            result = operations[choice](num1, num2)
            print("Result:", result)

        elif choice == "7":
            num = get_number("Enter a number: ")
            print("Result:", square_root(num))

        elif choice == "8":
            print("\n--- Calculation History ---")
            if history:
                for entry in history:
                    print(entry)
            else:
                print("No calculations yet.")

        elif choice == "9":
            print("Exiting... Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
