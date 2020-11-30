""" 8. Write a Python function that takes a list and returns a new list with unique
elements of the first list."""

print("Question 8")

l = [1,2,3,3,3,3,4,5]

def uniq_elem(l):
    return list(set(l))

print(uniq_elem(l))