import Addition
import Subtraction
import Multiplication
import Division

print("Select operation")
print("A.Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
print("E.All at once ")
while True:
    # take input from the user
    choice = input("Enter choice(A/B/C/D/E): ")
    choice = choice.upper()  # This Line Converts Lowercase To Uppercase ( Letters )

    # check if choice is one of the four options
    if choice in ('A', 'B', 'C', 'D', 'E'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'A':

            print(num1, "+", num2, "=", Addition.add(num1, num2))

        elif choice == 'B':

            print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))

        elif choice == 'C':
            print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))

        elif choice == 'D':

            print(num1, "/", num2, "=", Division.divide(num1, num2))

        elif choice == 'E':
            print('Operations on ', num1, " and ", num2)
            print('Sum = ', Addition.add(num1, num2))
            print('Difference = ', Subtraction.subtract(num1, num2))
            print('Product = ', Multiplication.multiply(num1, num2))
            print('Quotient = ', Division.divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        next_calculationt =next_calculation.lower()
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
