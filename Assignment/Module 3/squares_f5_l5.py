'''Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. '''

squares=[num ** 2 for num in range(1,31)]

print("List of squares : ")
print(squares)

print("squares of First 5 elements")
print(squares[:5])

print("squares of Last 5 elements")
print(squares[-5:])