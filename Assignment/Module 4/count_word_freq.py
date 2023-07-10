# Q. Write a Python program to count the frequency of words in a file. 

file = open("example.txt", 'r')

frequency = {}

words = file.read().split()

for word in words:
    if word in frequency:
        frequency[word] += 1
    elif word not in frequency:
        frequency[word] = 1

print(frequency)

