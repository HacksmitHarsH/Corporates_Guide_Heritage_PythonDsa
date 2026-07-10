
n = int(input())

# lists to store names and marks, and a variable for total marks
names = []
marks = []
total_marks = 0

# Loop N times to read each student's record
for i in range(n):
    # Read the line split it into name and mark
    record = input().split()
    student_name = record[0]
    student_mark = int(record[1])
    
    # Store them in our lists
    names.append(student_name)
    marks.append(student_mark)
    
    # Add the marks to our total sum
    total_marks += student_mark

#  Calculate the average mark
average_marks = total_marks / n

# Find students who scored greater than or equal to the average
eligible_students = []
for i in range(n):
    if marks[i] >= average_marks:
        eligible_students.append(names[i])

# Sort the eligible students names in alphabetical order
eligible_students.sort()

# Print each name on a new line to match the sample output
for name in eligible_students:
    print(name)