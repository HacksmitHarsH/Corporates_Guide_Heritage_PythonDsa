def check_voting_eligibility(age, is_citizen, is_registered):
    
    eligible = (age >= 18) and is_citizen and is_registered
    
    if eligible:
        print("The person is eligible to vote.")
    else:
        print("The person is not eligible to vote.")


check_voting_eligibility(8, True, True)