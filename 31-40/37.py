""" 37. Write a Python program to multiply all the items in a dictionary."""

print("Question 37")

dict = {'1':100,'2':50,'3':290}
multiple = 1

for items in dict.values():
    multiple = items * multiple

print(multiple)