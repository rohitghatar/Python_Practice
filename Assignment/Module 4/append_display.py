# Q. Write a Python program to append text to a file and display the text

file = open("example.txt", "a")

text = input("Enter text to append to the file: ")

# Append the text to the file
file.write(f"\n{text}")

print(f"appended text is = {text}")
file.close()

