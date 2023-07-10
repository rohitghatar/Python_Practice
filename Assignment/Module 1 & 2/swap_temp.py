'''Q. Write python program that swap two number with temp variable and
without temp variable.'''


# Swapping with a temporary variable
a = 55
b = 77

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


# Swapping without a temporary variable
a = 10
b = 5

print("Before swapping:")
print("a =", a)
print("b =", b)

a,b=b,a

print("After swapping:")
print("a =", a)
print("b =", b)
