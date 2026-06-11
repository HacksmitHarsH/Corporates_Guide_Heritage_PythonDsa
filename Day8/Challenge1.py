# a) Create a list of 10 student records. Each record is a tuple:
#    (student_name, roll_number, marks_list) where marks_list has 5 subject scores.
students_records = [
    ("Alice", 101, [85, 90, 78, 92, 88]),
    ("Bob", 102, [70, 65, 80, 72, 68]),
    ("Charlie", 103, [95, 98, 92, 96, 94]),
    ("Diana", 104, [60, 58, 62, 55, 64]),
    ("Ethan", 105, [82, 75, 88, 79, 81]),
    ("Fiona", 106, [45, 52, 61, 48, 50]),
    ("George", 107, [76, 84, 80, 78, 82]),
    ("Hannah", 108, [90, 92, 89, 94, 91]),
    ("Ian", 109, [66, 70, 68, 72, 65]),
    ("Julia", 110, [88, 85, 90, 87, 89])
]


# b) Write a function calculate_average(marks_list) that returns the average.
def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)


# c) Using list comprehension + your function, create a new list of tuples:
#    (name, average_score) for all students.
#    Note: We unpack the tuple in the comprehension, ignoring roll_number with an underscore (_).
students_averages = [(name, calculate_average(marks_list)) for name, _, marks_list in students_records]


# d) Sort this list by average score (descending) and print the class rank.
#    Note: key=lambda x: x[1] tells Python to sort based on the average score (index 1 of the tuple).
students_averages.sort(key=lambda student: student[1], reverse=True)

print("--- d) Class Rankings ---")
for rank, (name, avg) in enumerate(students_averages, start=1):
    print(f"Rank {rank}: {name} - Average: {avg:.2f}")
print()


# e) Print how many students scored above 75 average.
print("--- e) Students Above 75 Average ---")
# Count using a generator expression inside sum()
above_75_count = sum(1 for name, avg in students_averages if avg > 75)
print(f"Total students with an average above 75: {above_75_count}\n")


# f) Find and print the topper and the student with the lowest average.
print("--- f) Top and Bottom Performers ---")
# Since the list is already sorted in descending order:
# - The first item (index 0) is the topper.
# - The last item (index -1) has the lowest average.
topper_name, topper_avg = students_averages[0]
lowest_name, lowest_avg = students_averages[-1]

print(f"Class Topper: {topper_name} with an average of {topper_avg:.2f}")
print(f"Lowest Performer: {lowest_name} with an average of {lowest_avg:.2f}")