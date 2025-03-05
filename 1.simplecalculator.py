# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2==0:
        return "Error! Division by zero."
    else:
        return num1/num2


# Main program
def simple_calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        # Get user input for operation choice
        choice = int(input("Choice operations Between 1 and 5: "))

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break

        try:
            number_1 = eval(input("Enter first number: "))
            number_2 = eval(input("Enter second number: "))

        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform the operation
        if choice == 1:
            print(number_1, "+", number_2, "=",add(number_1, number_2))

        elif choice == 2:
            print(number_1, "-", number_2, "=",subtract(number_1, number_2))

        elif choice == 3:
            print(number_1, "*", number_2, "=",multiply(number_1, number_2))

        elif choice == 4:
            print(number_1, "/", number_2, "=",divide(number_1, number_2))
        else:
            print("Invalid input! Please choose a valid operation.")

# Run the calculator
simple_calculator()
