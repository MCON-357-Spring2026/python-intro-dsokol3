"""
TODO:
Dictionary of students -> grades
Print averages
"""
students = {
    "Alice": [80, 85.5, 90],
    "Bob": [90, 91, 92.5]
}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name}: {avg:.2f}")

