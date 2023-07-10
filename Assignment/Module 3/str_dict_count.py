'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource' '''

# 1st method

sample_string = 'w3resource'

letter_count = {}

for letter in sample_string:
    letter_count[letter] = letter_count.get(letter, 0) + 1


print("Letter count dictionary:", letter_count)


# 2nd method

from collections import Counter

sample_string1 = 'w3resource'

letter_count2 = Counter(sample_string1)
    
print("Letter count dictionary:", letter_count2)
