""" 33. Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys."""

print("Question 33")

num = 15
dict = dict()

for x in range(1, num+1):
    dict[x] = x*x

print(dict)