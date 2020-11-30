""" 2. Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string. """
print("Question 2")
str = input("Enter String Only: ")
str_new = ""

if len(str) < 2:
    str_new = ""
else:
    str_new = str[0]+str[1]+str[-2]+str[-1]
print(str_new)



