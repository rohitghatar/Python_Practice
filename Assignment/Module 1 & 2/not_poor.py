'''Q. Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

string = input("Enter a string: ")

index_not = string.find('not')

index_poor = string.find('poor')

if index_not != -1 and index_poor != -1:
    if index_not < index_poor:
        new_string = string[:index_not] + 'good' + string[index_poor+4:]
    else:
        new_string = string
else:
    new_string = string

print("Resulting string:", new_string)
