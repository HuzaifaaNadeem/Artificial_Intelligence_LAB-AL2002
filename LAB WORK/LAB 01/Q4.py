while True:
    print("\n1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == 3:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
