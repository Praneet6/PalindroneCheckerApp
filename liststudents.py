# List of student dictionaries
students = [
    {"name": "Aditi", "cgpa": 9.1},
    {"name": "Rahul", "cgpa": 7.8},
    {"name": "Priya", "cgpa": 8.5},
    {"name": "Karan", "cgpa": 6.9}
]

# Function that accepts a condition function (criteria)
def filter_students(criteria, students):
    return [s for s in students if criteria(s)]

# Using lambda as criteria
high_cgpa_students = filter_students(lambda s: s["cgpa"] > 8, students)

print("Students with CGPA > 8:")
for s in high_cgpa_students:
    print(s["name"], "-", s["cgpa"])
