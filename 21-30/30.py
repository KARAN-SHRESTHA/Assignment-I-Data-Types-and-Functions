""" 30. Write a Python script to check whether a given key already exists in a
dictionary."""

print("Question 30")

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def check_key(k):
    if k in dic:
        print("Exists")
    else:
        print("Doesnt")


check_key(5)

