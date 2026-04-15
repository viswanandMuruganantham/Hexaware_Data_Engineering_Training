# Factorial of a number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("Factorial is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "is", factorial)