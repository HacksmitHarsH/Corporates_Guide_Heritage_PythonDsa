special_characters = "!@#$%^&*(),.?\":{}|<>"
attempts = 0

while True:
    password = input("Enter a password to evaluate: ")
    attempts += 1
    
    # Initialize criteria flags
    has_length = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Check each character using loops and control statements
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
            
    # Calculate score based on total criteria met
    criteria_met = [has_length, has_upper, has_lower, has_digit, has_special]
    score = sum(criteria_met)
    
    # Display individual criteria status
    print("\n--- Criteria Breakdown ---")
    print(f"[{'✓' if has_length else 'X'}] Minimum 8 characters")
    print(f"[{'✓' if has_upper else 'X'}] At least one uppercase letter")
    print(f"[{'✓' if has_lower else 'X'}] At least one lowercase letter")
    print(f"[{'✓' if has_digit else 'X'}] At least one digit")
    print(f"[{'✓' if has_special else 'X'}] At least one special character")
    
    # Determine strength rating
    if score == 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"
        
    print(f"Password Rating: {rating} ({score}/5 criteria met)")
    print("-" * 30)
    
    # Break condition for strong password
    if rating == "Strong":
        print(f"Success! Secure password accepted on attempt #{attempts}.\n")
        break
    else:
        print("Password is not strong enough. Please try again.\n")