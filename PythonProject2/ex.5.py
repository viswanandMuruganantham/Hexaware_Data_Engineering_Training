emails = [
"user1@gmail.com",
"user2@yahoo.com",
"user3@gmail.com",
"user4@outlook.com"
]
freq = {}
for email in emails:
    domian = email.split("@")[1]
    print(domian)
    if domian in freq:
        freq[domian] += 1
    else:
        freq[domian] = 1
print(freq)
