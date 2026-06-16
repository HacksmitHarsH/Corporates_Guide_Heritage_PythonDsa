student1 = {"Math", "Physics", "Chemistry", "English"}
student2 = {"Math", "Biology", "English", "History"}

# 1. Common subjects (Intersection)
common = student1 & student2
print(f"Common subjects: {common}")

# 2. Subjects only taken by Student 1 (Difference)
only_student1 = student1 - student2
print(f"Subjects only taken by Student 1: {only_student1}")

# 3. Subjects only taken by Student 2 (Difference)
only_student2 = student2 - student1
print(f"Subjects only taken by Student 2: {only_student2}")