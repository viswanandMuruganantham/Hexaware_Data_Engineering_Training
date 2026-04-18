inventory = {
"laptop":10,
"mouse":25,
"keyboard":15
}

inventory["monitor"] = 8
print(inventory)
inventory["laptop"] -= 2
for key , value in inventory.items():
    if value < 10:
        print(key)
