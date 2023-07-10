# Q. Write a Python program to get the Fibonacci series of given range.

range_limit = int(input("Enter the range limit: "))

num1 = 0
num2 = 1


while num2 <= range_limit:
    next_num = num1 + num2
    if next_num <= range_limit:
        print(next_num)
    
    num1 = num2
    num2 = next_num