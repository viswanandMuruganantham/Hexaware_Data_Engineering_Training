from studentss import load_students, analysis, write_unique_students
from marks import load_marks, analyze_marks
from attendance import load_attendance, calculate_attendance_percentage
from analytics import (
    create_mark_dict,
    best_attendance,
    generate_grade,
    combine_data,
    eligible_students,
    improvement_students
)


def main():
    students = load_students("students.txt")
    total, unique, count_dict = analysis(students)
    write_unique_students(unique)

    marks_data = load_marks("marks.json")
    highest, lowest, avg, python_students, course_count = analyze_marks(marks_data)

    attendance = load_attendance("attendance.csv")
    attendance_percent = calculate_attendance_percentage(attendance)

    combined = combine_data(marks_data, attendance_percent)

    topper = highest["name"]
    best_att = best_attendance(attendance_percent)

    eligible = eligible_students(combined)
    improvement = improvement_students(combined)

    # Write report
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("Student Report\n")

        for name, data in combined.items():
            grade = generate_grade(data["marks"])
            f.write(f"{name} - Marks: {data['marks']} - Attendance: {data['attendance']:.1f}% - Grade: {grade}\n")

    # Eligible file
    with open("eligible_students.txt", "w", encoding="utf-8") as f:
        for name in eligible:
            f.write(name + "\n")

    # Final Output
    print("Topper:", topper)
    print("Best Attendance:", best_att)
    print("Average Marks:", round(avg, 1))
    print("Eligible Students:", ", ".join(eligible))
    print("Students Needing Improvement:", ", ".join(improvement))


if __name__ == "__main__":
    main()