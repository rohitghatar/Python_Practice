# Write a Python function that takes a list of words and returns the length of the longest one.

def max_length(list_of_words):
    for i in range(list_of_words):
        

words = []

num_of_words = int(input("how many words you want to insert : "))

for i in range(1, num_of_words+1):
    your_word = input(f"enter your {i} word : ")
    words.append(your_word)

