# Write a Python function to insert a string in the middle of a string.

def string(main_string, string_to_insert):
    mid_index = len(main_string) // 2
    print(main_string[:mid_index] + string_to_insert + main_string[mid_index:])

main_string = "Hello  there"
string_to_insert = "Python"
string(main_string, string_to_insert)

