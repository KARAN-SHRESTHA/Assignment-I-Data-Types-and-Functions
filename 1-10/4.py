""" 4. Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string."""

print("Question 4")
str = "abc"
str1 = "xyz"

new_value = str1[:2] + str[2:]
new_value1 = str[:2] + str1[2:]

print(new_value + " " + new_value1)
