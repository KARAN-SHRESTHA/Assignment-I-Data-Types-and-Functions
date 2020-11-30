""" 15. Write a Python program to filter a list of integers using Lambda."""

print("Question 15")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("EVEN NUMBERS  ", list(filter(lambda x : x%2 == 0, nums)))

print("ODD NUMBERS  ", list(filter(lambda x : x%2 != 0, nums)))