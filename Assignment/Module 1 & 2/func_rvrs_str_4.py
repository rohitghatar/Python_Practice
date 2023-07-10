# Write a Python function to reverses a string if its length is a multiple of 4.

def reverse_string(string):
    if len(string) % 4 == 0:
        print(string[::-1]) 
    else:
        print(string) 


input_string = input("Enter a string: ")
reverse_string(input_string)

