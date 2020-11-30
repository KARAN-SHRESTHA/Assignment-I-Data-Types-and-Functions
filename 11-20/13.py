""" 13. Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically)."""

print("Question 13")

str = input("Enter String with seperating ',' ")

words = str.split(',')

print(",".join(sorted(list(set(words)))))
