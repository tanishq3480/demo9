import Addition
import Subtraction
import Multiplication
import Division

print("Select operation\n")
print("A.Add\n")
print("B.Subtract\n")
print("C.Multiply\n")
print("D.Divide\n")
print("E All at once\n")
while True:
    # take input from the user
    choice = input("Enter choice(A/B/C/D): \n")

    # check if choice is one of the four options
    if choice in ('A', 'B', 'C', 'D', 'E'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if choice == 'A' or choice == 'a':
        print(num1, "+", num2, "=", Addition.add(num1, num2))

    elif choice == 'B' or 'b':
        print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))

    elif choice == 'C' or 'c':
        print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))

    elif choice == 'D' or 'd':
        print(num1, "/", num2, "=", Division.divide(num1, num2))
    # elif choice == 'E' or choice == 'e':
    #     print('All operations at once')
    #     print(num1, "+", num2, "=", Addition.add(num1, num2))
    #     print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))
    #     print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))
    #     print(num1, "/", num2, "=", Division.divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
else:
    print("Invalid Input")
