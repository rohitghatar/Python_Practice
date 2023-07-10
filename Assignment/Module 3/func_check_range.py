# Write a Python function to check whether a number is in a given range

#----- 1st method ----------------

def check_in_range(number, start, end):
    
    
    if start <= number <= end:
        print(num, "is in the range", range_start, "-", range_end)
    else:
        print(num, "is not in the range", range_start, "-", range_end)

num = 5
range_start = 1
range_end = 10
check_in_range(num, range_start, range_end)


#------------ 2nd Method ---------------------

def check_in_range2(number, start, end):
    return start <= number <= end

num = 7
range_start, range_end = 1, 10
in_range = check_in_range2(num, range_start, range_end)

print(f"{num} is {'in' if in_range else 'not in'} the range {range_start} - {range_end}")
