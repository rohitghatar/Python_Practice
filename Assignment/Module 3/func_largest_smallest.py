'''Write a Python function to get the largest number, smallest num and sum
of all from a list. '''

def analyze_numbers(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    return largest, smallest, total

num_list = [10, 5, 8, 12, 3, 7]
largest_num, smallest_num, sum_of_all = analyze_numbers(num_list)
print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", sum_of_all)
