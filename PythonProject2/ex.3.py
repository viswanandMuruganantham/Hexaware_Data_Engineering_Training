students = {
"Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}
topper = max(students, key = students.get)
print(topper)

average = sum(students.values()) / len(students)
print(average)
for name, marks in students.items():
    if marks > 85:
        print("Above 85:", name)

