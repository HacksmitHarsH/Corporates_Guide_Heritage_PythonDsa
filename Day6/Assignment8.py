

age = int(input("Enter age: "))
tickets = int(input("Enter number of tickets: "))

# Determine price per ticket based on age
if age >= 18:
    if age >= 60:
        
        price_per_ticket = 100
    else:
        
        price_per_ticket = 200
else:
    if age < 10:
        
        price_per_ticket = 50
    else:
       
        price_per_ticket = 100


total_price = price_per_ticket * tickets

if tickets > 10:
    discount = total_price * 0.20
    final_price = total_price - discount
    print(f"Age: {age}")
    print(f"Tickets: {tickets}")
    print(f"Price per ticket: Rs. {price_per_ticket}")
    print(f"Total price: Rs. {total_price}")
    print(f"Group discount (20%): Rs. {discount}")
    print(f"Final price: Rs. {final_price}")
else:
    print(f"Age: {age}")
    print(f"Tickets: {tickets}")
    print(f"Price per ticket: Rs. {price_per_ticket}")
    print(f"Final price: Rs. {total_price}")