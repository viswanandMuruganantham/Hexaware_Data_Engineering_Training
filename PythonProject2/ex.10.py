logins = [
("Rahul","10:00"),
("Sneha","10:10"),
("Rahul","11:00"),
("Arjun","11:15"),
("Sneha","11:30")
]
freq = {}
for key, value in logins:
    if key in freq:
        freq[key] += 1
    else:
        freq[key] = 1
print(freq)