history = []

while True:
    print("\n========== MENU ==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Quit")
    print("==========================")
    
    choice = input("Select an option (1-6): ").strip()
    
    if choice == "6":
        print("\n--- Calculation History ---")
        if not history:
            print("No operations performed in this session.")
        else:
            for record in history:
                print(record)
        print("\nThank you for using the calculator. Goodbye!")
        break
        
    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice! Please select a valid option from the menu.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid numeric input. Returning to menu.")
        continue

    if choice == "1":
        result = num1 + num2
        operation = f"{num1} + {num2} = {result}"
        print(f"Result: {operation}")
        history.append(operation)
        
    elif choice == "2":
        result = num1 - num2
        operation = f"{num1} - {num2} = {result}"
        print(f"Result: {operation}")
        history.append(operation)
        
    elif choice == "3":
        result = num1 * num2
        operation = f"{num1} * {num2} = {result}"
        print(f"Result: {operation}")
        history.append(operation)
        
    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            operation = f"{num1} / {num2} = {result}"
            print(f"Result: {operation}")
            history.append(operation)
            
    elif choice == "5":
        result = num1 ** num2
        operation = f"{num1} ^ {num2} = {result}"
        print(f"Result: {operation}")
        history.append(operation)