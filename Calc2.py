import Addition
import Subtraction
import Multiplication
import Division

print("Select operation")
print("A.Add")
print("B.Subtract")
print("C.Multiply")
print("D.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(A/B/C/D): ")

    # check if choice is one of the four options
    if choice in ('A', 'B', 'C', 'D'):
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
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
