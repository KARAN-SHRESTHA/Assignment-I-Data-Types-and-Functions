""" 10. Write a Python program to print the even numbers from a given list."""

print("Question 10")

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_even(l):
    l1 = []
    for i in l:
        if i % 2 == 0:
           l1.append(i)
    print(l1)

print_even(l)