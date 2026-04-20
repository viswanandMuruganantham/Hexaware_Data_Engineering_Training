def load_students(filename):
    students = []
    with open("students.txt", "r") as read_file:
        for line in read_file:
            students.append(line.strip())
    return students
def analysis(students):
    total = len(students)
    uni = set(students)
    count_dict = {}
    for s in students:
        if s in count_dict:
            count_dict[s] += 1
        else:
            count_dict[s] = 1
    return total, uni, count_dict
def write_unique_students(unique_students):
    with open("unique_students.txt", "w", encoding="utf-8") as f:
        for name in unique_students:
            f.write(name + "\n")
