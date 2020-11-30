""" 9. Write a Python program to change a given string to a new string where the first
and last chars have been exchanged."""

print("Question 9")


def ex_char(str):
    first_char = str[0]
    last_char = str[-1]
    new_char = last_char + str[1:-1] + first_char
    return new_char


print(ex_char(input("Enter a String.")))
