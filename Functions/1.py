""" 1. Write a Python function to find the Max of three numbers."""

print("Question 1")

first_num = int(input("Enter First Number:  "))
second_num = int(input("Enter Second Number:  "))
third_num = int(input("Enter Three Number:  "))
l = []


def find_max():
    l = [first_num, second_num, third_num]
    return max(l)

print(find_max())
