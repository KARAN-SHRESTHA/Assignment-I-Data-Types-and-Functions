""" 13. Write a Python program to sort a list of tuples using Lambda."""

print("Question 13")

tup = 'karan', 'sita', 'hari', 'vishnu', 'shiva'

lam = lambda tup : sorted(tup)

print(lam(tup))