# Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'a': 5, 'b': 2, 'c': 10, 'd': 3, 'e': 7}

#----- Mymethod-----------

list1= my_dict.values()
list2= my_dict.keys()

ascend = list(sorted(zip(list1,list2)))
decend = list(sorted(zip(list1,list2), reverse=True))
print(ascend)
print(decend)


#---- 1st method -----------------------------

my_dict = {'a': 5, 'b': 2, 'c': 10, 'd': 3, 'e': 7}

sorted_dict_asc = dict(sorted(my_dict.items()))

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Sorted Dictionary (Ascending):", sorted_dict_asc)
print("Sorted Dictionary (Descending):", sorted_dict_desc)


#------- 2nd method ------------------------------


sorted_dict_asc2 = dict(sorted(my_dict.items(), key=lambda x: x[1])) 

sorted_dict_desc2 = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print("Sorted Dictionary (Ascending):", sorted_dict_asc2)
print("Sorted Dictionary (Descending):", sorted_dict_desc2)
