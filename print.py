def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

print("Welcome to the Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

    choice = input("Enter your choice (0-4): ")

    if choice == '0':
        print("Exiting the Calculator. Goodbye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please try again.")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operator = '*'
    else:
        result = divide(num1, num2)
        operator = '/'

    print(f"\n{num1} {operator} {num2} = {result}")
