def insert_string_in_middle(main_string, string_to_insert):
    mid_index = len(main_string) // 2
    return main_string[:mid_index] + string_to_insert + main_string[mid_index:]

# Example usage
main_string = "Hello World"
string_to_insert = "Python"
result = insert_string_in_middle(main_string, string_to_insert)
print("Result:", result)
