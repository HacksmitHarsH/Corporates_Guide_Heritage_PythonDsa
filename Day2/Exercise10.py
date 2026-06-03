# Data points
name = "Harsh Ashthana"
raw_id = "505"
dept = "Marketing"
raw_salary = "82000.00"
is_manager = True

# Type casting
emp_id = int(raw_id)
salary = float(raw_salary)

# Summary Report
print(f"{'--- EMPLOYEE SUMMARY ---':^30}")
print(f"Name:       {name}")
print(f"ID:         {emp_id:06}")
print(f"Department: {dept}")
print(f"Salary:     ${salary:,.2f}")
print(f"Manager:    {'Yes' if is_manager else 'No'}")