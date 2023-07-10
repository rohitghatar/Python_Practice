# Q Write a python program to find the longest words

file = open("example.txt", 'r')

words = file.read().split()

max_length = max(len(word) for word in words)

longest_word = [word for word in words if len(word) == max_length]

print(longest_word)