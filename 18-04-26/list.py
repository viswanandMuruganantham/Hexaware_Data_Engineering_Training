numbers = [10,20,30,40,50]
print(numbers)

fruits = ['apple','banana','mango']
print(fruits)
print(fruits[0])
print(fruits[-1])

numbers[1] = 200
print(numbers)

numbers.append(100)
print(numbers)

numbers.insert(1,1000)
print(numbers)

numbers.remove(10)
print(numbers)

print(numbers[1:4])

print(numbers.reverse())
print("reverse",numbers)

numbers.sort()
print(numbers)

print(max(numbers))
print(min(numbers))

numbers.pop()
print(numbers)

for number in numbers:
    print(number)

if "apple" in fruits:
    print("apple exists")