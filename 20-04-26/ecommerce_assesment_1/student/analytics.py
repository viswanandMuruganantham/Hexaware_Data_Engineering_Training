def create_mark_dict(students):
    return {s["name"]: s["marks"] for s in students}


def best_attendance(attendance_percent):
    return max(attendance_percent, key=attendance_percent.get)


def generate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"


def combine_data(students, attendance_percent):
    combined = {}

    for s in students:
        name = s["name"]
        combined[name] = {
            "marks": s["marks"],
            "attendance": attendance_percent.get(name, 0),
            "course": s["course"]
        }

    return combined


def eligible_students(combined):
    return [
        name for name, data in combined.items()
        if data["marks"] >= 75 and data["attendance"] >= 80
    ]


def improvement_students(combined):
    return [
        name for name, data in combined.items()
        if data["marks"] < 75 or data["attendance"] < 80
    ]