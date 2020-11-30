""" 10. Write a Python program to remove the characters which have odd index
values of a given string."""

print("Question 10")

str = "SHRESTHA"

new_char = ''
for items in range(len(str)):
    if items % 2 == 0:
        new_char += str[items]

new_char = new_char[1:]
print(new_char)
