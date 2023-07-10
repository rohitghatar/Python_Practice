'''Q. Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''


string = input("Enter a string: ")

if len(string) >= 3:
    if string.endswith('ing'):
        new_string = string + 'ly'
    else:
        new_string = string + 'ing'
else:
    new_string = string

print("Modified string:", new_string)
