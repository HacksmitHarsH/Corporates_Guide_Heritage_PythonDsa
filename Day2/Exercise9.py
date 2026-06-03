employees = [("Harsh Ashthana", 202601), ("Rishu Kumar", 202602), ("Aditya Raj", 202603)]

print(f"{'Name':<20} | {'ID':>6}")
print("-" * 30)
for name, eid in employees:
    print(f"{name:<20} | {eid:06d}")