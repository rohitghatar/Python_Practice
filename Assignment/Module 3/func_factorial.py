'''Write a Python function to calculate the factorial of a number (a
nonnegative integer) '''

def factorial(n):
    if n < 0:
        print("Factorial is undefined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        print("Factorial of", n, "is", result)

number = 10
factorial(number)

