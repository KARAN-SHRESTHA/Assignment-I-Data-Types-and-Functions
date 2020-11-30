"""3. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself."""

print("Question 3")
str = "restart"

char = str[0]
str = str.replace(char, '$')
str = char + str[1:]
print(str)