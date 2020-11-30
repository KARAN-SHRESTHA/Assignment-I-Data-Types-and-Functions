""" 43. Write a Python program to remove an item from a tuple."""

print("Question 43")

tup = ('K', 'a', 'r', 'a', 'n')
tup1 = tuple()

def remove_tup(i):
    tup1 = tup[:i] + tup[i+1:]
    return tup1

print(remove_tup(int(input("Enter Index Number:  "))))