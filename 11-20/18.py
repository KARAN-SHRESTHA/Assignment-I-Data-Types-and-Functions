""" 18. Write a Python program to get the largest number from a list."""

print("Question 18")

mylist = [ 10, 25, 5, 8, 7, 21, 2]


def check_length(my_list):
    char_len = my_list[0]
    for items in my_list:
        if items > char_len:
            char_len = items
    return char_len


print(check_length(mylist))