""" 3. Write a Python function to multiply all the numbers in a list."""

print("Question 3")

l = [8, 2, 3, -1, 7]


def multiple_list(l):
    multiple = 1
    for items in l:
        multiple = multiple * items
    return multiple

print(multiple_list(l))


