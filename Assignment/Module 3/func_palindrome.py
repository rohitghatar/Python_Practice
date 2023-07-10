# Write a Python function that checks whether a passed string is palindrome or not

#---- 1st method ----------

def is_palindrome(string):
    normalized_string = string.lower().replace(" ", "")
    reversed_string = normalized_string[::-1]
    return normalized_string == reversed_string

word = "level"
is_palindrome_word = is_palindrome(word)

if is_palindrome_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


#------------- 2nd Method ------------

def is_palindrome(string):
    return string.lower().replace(" ", "") == string.lower().replace(" ", "")[::-1]

word = "level"
is_palindrome_word = is_palindrome(word)

message = f"{word} is {'a palindrome.' if is_palindrome_word else 'not a palindrome.'}"
print(message)

