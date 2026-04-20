import json
def load_marks(filename):
    with open(filename, "r") as file_read:
        data = json.load(file_read)
    return data["students"]
def analyze_marks(students):
    highest = students[0]
    for s in students:
        if s["marks"] > highest["marks"]:
            highest = s
    lowest = min(students, key=lambda x: x["marks"])

    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    python_students = [s for s in students if s["course"] == "Python"]

    course_count = {}
    for s in students:
        course = s["course"]
        course_count[course] = course_count.get(course, 0) + 1

    return highest, lowest, avg, python_students, course_count