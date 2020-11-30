""" 16. Write a Python program to square and cube every number in a given list of
integers using Lambda."""

l = [1,2,3,4,5,6]

print("Square of items:  ", list(map(lambda x:x**2, l)))
print("Cube of items:  ", list(map(lambda x:x**3, l)))