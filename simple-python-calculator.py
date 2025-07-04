# Exersice 1
while True:
        print("\nWellcome to Calculator.")
        
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        operation = input("Enter The Symbol Of Operation (+, -, *, /, **): ")

        if (operation == "+"):
                print("\nLet's Calculate !!!")
                print(f"Addition of {num1} and {num2} is {num1 + num2}" )

        elif (operation == "-" ):
                print("\nLet's Calculate !!!")
                print(f"Subtraction of {num1} and {num2} is {num1 - num2}")

        elif (operation == "*"):
                print("\nLet's Calculate !!!")
                print(f"Multiplication {num1} and {num2} is {num1 * num2}")

        elif (operation == "/"):
                print("\nLet's Calculate !!!")
                if (num2 == 0):
                        print("❌ Error: Division by zero is not allowed.")
                else:
                        print(f"Division of {num1} by {num2} is {num1 / num2}")


        elif (operation =="**"):
                print(f"\n{num1} raised to the power {num2} is {num1 ** num2}") 

        else :
                print("\nrror : Invalid Operation. Please enter the symbol of the operation")

        print("Thank You.....")

        repeat  = input("Do you want to stop the programm? (yes/no)\n")
        if (repeat == "yes"):
                print("👋 Thank you for using the calculator!")
                break