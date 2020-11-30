""" 23. Write a Python program to check a list is empty or not."""

print("Question 23")

l1 = []
l2 = ['ram', 'sita', 'hari', 'ram', 'sita', 'gita']


def check_list(l):
    if not l:
        print("LIST EMPTY")
    else:
        print("LIST NOT EMPTY")


print(check_list(l1))

