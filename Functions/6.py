"""6. Write a Python function to check whether a number is in a given range."""

print("Question 6")


def check_range(num):
    return num in range(1,10)


print(check_range(int(input("Enter Number:  "))))