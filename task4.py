def display_menu():
    print("Simple Command-Line Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_user_choice():
    return input("Enter your choice (1/2/3/4/5): ")

def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def validate_choice(choice):
    return choice in ["1", "2", "3", "4", "5"]

def validate_numbers(num1, num2, operation):
    if operation == "4" and num2 == 0:
        print("Error: Division by zero is not allowed.")
        return False
    return True

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if not validate_choice(choice):
            print("Invalid choice. Please choose a valid operation.")
            continue

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        num1, num2 = get_numbers()

        if not validate_numbers(num1, num2, choice):
            continue

        if choice == "1":
            print(f"The result of addition is: {add(num1, num2)}")
        elif choice == "2":
            print(f"The result of subtraction is: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"The result of multiplication is: {multiply(num1, num2)}")
        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print(f"The result of division is: {result}")

if __name__ == "__main__":
    main()
