'''Q. Write a Python program to count the number of characters (character
frequency) in a string'''

string = input("Enter a string: ")

char_frequency = {}

for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

for char, frequency in char_frequency.items():
    print(char, ":", frequency)


print(char_frequency)