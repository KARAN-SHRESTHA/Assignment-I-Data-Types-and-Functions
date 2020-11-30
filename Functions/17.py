""" 17. Write a Python program to find if a given string starts with a given character
using Lambda."""

print("Question 17")

str = 'Karan'

chk = lambda x, y : y in x[0].lower()

print(chk(str, 'k'))