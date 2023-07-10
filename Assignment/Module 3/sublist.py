# Write a Python program to check whether a list contains a sub list

main_list = [1, 2, 3, 4, 5, 6, 7]
sub_list = [3, 8, 5]

'''main_len = len(main_list)
sub_len = len(sub_list)'''


'''for i in range(main_len - sub_len + 1):
    if main_list[i:i+sub_len] == sub_list:
        found = True
        break'''

tmp=[]
for i in sub_list:
    if i in main_list:
        tmp.append(i)


if sub_list == tmp:
    print("The list contains the sub list.")
else:
    print("The list does not contain the sub list.")


