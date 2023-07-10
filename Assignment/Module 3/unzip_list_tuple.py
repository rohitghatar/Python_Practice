# Write a Python program to unzip a list of tuples into individual lists. 

list_of_tuples = [(1, 4), (2, 5), (3, 6)]

unzipped_lists = list(zip(*list_of_tuples))

print("Unzipped lists:", unzipped_lists)
