""" 32. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x)."""

print("Question 32")

num = int(input("Input a number "))
dict = dict()

for x in range(1, num+1):
    dict[x] = x*x

print(dict)
