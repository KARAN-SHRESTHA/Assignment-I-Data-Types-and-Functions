""" 11. Write a Python program to count the occurrences of each word in a given
sentence."""

print("Question 11")

str = "His name is Ram and her name is Sita."

count = dict()
words = str.split()

for items in words:
    if items in count:
        count[items] += 1
    else:
        count[items] = 1
print(count)
