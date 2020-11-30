""" 25. Write a Python program to check whether all dictionaries in a list are empty or
not."""

print("Question 25")

l1 : [{},{},{}]

l2: [{1,2},{},{}]

print(all(not d for d in l1))
print(all(not d for d in l2))