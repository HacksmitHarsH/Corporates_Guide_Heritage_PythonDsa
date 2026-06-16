# Create a dictionary with 5 students and their marks
student_marks = {
    "Rahul": 85,
    "Amit": 78,
    "Priya": 92,
    "Sneha": 88,
    "Karan": 69
}

# 1. Print all student names
names = list(student_marks.keys())
print(f"Student Names: {names}")

# 2. Print all marks
marks = list(student_marks.values())
print(f"Marks: {marks}")

# 3. Find the average mark of all students
total_marks = sum(student_marks.values())
num_students = len(student_marks)
average_marks = total_marks / num_students

print(f"Average Marks: {average_marks:.1f}")