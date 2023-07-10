# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list():
    list1 = []
    unique_list = []

    n = int(input("enter the number of items you want : "))

    for i in range(n):
        input_list = input("Enter list item : ")
        list1.append(input_list)

    for i in list1:
        if i not in unique_list:
            unique_list.append(i)

    print("Your Entered list : ",list1)
    print("List with unique member : ",unique_list)

unique_list()