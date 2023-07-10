# Write a Python program to read a random line from a file

import random

def read_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()

file_path = 'sample.txt'  # Replace with the path to your file
random_line = read_random_line(file_path)
print("Random Line:", random_line)
