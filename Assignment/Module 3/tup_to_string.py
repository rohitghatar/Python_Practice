# Write a Python program to convert a tuple to a string. 

#   method 1
'''my_tuple = ("Hello", "World", "Python")

my_string = ' '.join(str(element) for element in my_tuple)

print(my_string)'''

#   method 2
my_tuple = ('Hello', 'World', 'Python')

result = " + ".join(my_tuple)

print(my_tuple)
print(result)
