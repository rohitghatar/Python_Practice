# Write a python program to sum of the first n positive integers.

n = int(input("Enter a positive integer: "))

# Check if n is a positive integer
if n <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print("The sum of the first", n, "positive integers is:", sum)
