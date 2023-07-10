# Write a Python function that takes a list of words and returns the length of the longest one.

def check_length(word_list):
    max_length = 0

    for word in word_list:
        length = len(word)
        if length > max_length:
            max_length = length

    print(max_length)



words=(['word','12345678','123','12345'])

check_length(words)

