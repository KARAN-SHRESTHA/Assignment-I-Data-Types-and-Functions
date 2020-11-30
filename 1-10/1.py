""" 1. Write a Python program to count the number of characters (character
frequency) in a string. Sample String : www.google.com """

print("Question 1")

str = "www.google.com"
count = dict()

for items in str:
    if items in count:
        count[items] += 1
    else:
        count[items] = 1

print(count)