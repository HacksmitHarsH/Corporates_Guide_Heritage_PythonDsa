# --- Requirement 1: Store student details (ID, Name, Course) ---

student_details = {
    1001: {"name": "Arjun", "course": "Data Science"},
    1002: {"name": "Meera", "course": "Web Development"},
    1003: {"name": "Kabir", "course": "Machine Learning"}
}


# --- Requirement 2: Store unique course categories ---

course_categories = {"Programming", "Design", "Business", "Marketing"}


# --- Requirement 3: Store course ratings for multiple courses ---

course_ratings = [
    {"course_name": "Python 101", "rating": 4.8},
    {"course_name": "UI/UX Basics", "rating": 4.5},
    {"course_name": "AI Basics", "rating": 4.9}
]

# Quick verification print output
print("Student Details Example ID 1001:", student_details[1001])
print("Categories:", course_categories)
print("First Rated Course:", course_ratings[0])