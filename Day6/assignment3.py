username=input("Enter your username: ")
account_status=input("Enter your account status (active/inactive): ")
password=input("Enter your password: ")

if username == 'admin':
    if account_status.lower() == 'active':
        if password == 'admin123':
            print("Welcome, admin!")
        else:
            print("Incorrect password.")
    else:
        print("Account inactive.")
else:
    print("Access denied.")