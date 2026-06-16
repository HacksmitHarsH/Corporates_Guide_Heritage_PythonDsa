event1 = {"Aman", "Riya", "Karan", "Neha"}
event2 = {"Neha", "Riya", "Vikas", "Rohan"}

# 1. Attendees registered for both events (Intersection)
both_events = event1.intersection(event2)
print(f"Registered for both events: {both_events}")

# 2. Attendees registered for exactly one event (Symmetric Difference)
exactly_one = event1.symmetric_difference(event2)
print(f"Registered for exactly one event: {exactly_one}")

# 3. Count the total unique attendees (Union and len)
total_unique = event1.union(event2)
print(f"Total unique attendees count: {len(total_unique)}")