""" 7. Write a Python function that takes a list of words and returns the length of the
longest one."""
print("Question 7")

mylist = ['My', 'Shrestha', 'is', 'name', 'Karan']


def check_length(my_list):
    char_len = 0
    for items in my_list:
        if len(items) > char_len:
            char_len = len(items)
    return char_len


print(check_length(mylist))

