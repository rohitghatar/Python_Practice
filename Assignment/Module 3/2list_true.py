# Write a Python function that takes two lists and returns true if they have at least one common member.

list1 = []
list2 = []

for i in range(3):
    item = input("Enter 1st list item : ")
    list1.append(item)


for i in range(3):
    item = input("Enter 2st list item : ")
    list2.append(item)

for i in list2:
    if i in list1:
        print(True)
        break