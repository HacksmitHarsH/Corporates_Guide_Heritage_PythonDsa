PIN = "1234"
balance = 10000.0

print("Welcome to the ATM system")
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == PIN:
    while True:
        print("\nMain Menu")
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Select an option (1-4): ")
        match choice:
            case "1":
                print(f"Your current balance is: ₹{balance:.2f}")
            case "2":
                amount_str = input("Enter amount to withdraw: ")
                if amount_str.replace('.', '', 1).isdigit():
                    amount = float(amount_str)
                    if amount > 0:
                        if amount <= balance:
                            balance -= amount
                            print(f"Please collect your cash. New balance: ₹{balance:.2f}")
                        else:
                            print("Insufficient funds.")
                    else:
                        print("Withdraw amount must be positive.")
                else:
                    print("Invalid amount entered.")
            case "3":
                amount_str = input("Enter amount to deposit: ")
                if amount_str.replace('.', '', 1).isdigit():
                    amount = float(amount_str)
                    if amount > 0:
                        balance += amount
                        print(f"Deposit successful. New balance: ₹{balance:.2f}")
                    else:
                        print("Deposit amount must be positive.")
                else:
                    print("Invalid amount entered.")
            case "4":
                print("Thank you for using the ATM. Goodbye.")
                break
            case _:
                print("Invalid option. Please try again.")
else:
    print("Invalid PIN. Access denied.")
