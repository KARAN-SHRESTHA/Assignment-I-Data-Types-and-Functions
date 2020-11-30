"""7. Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters."""

print("Question 7")

str = 'The quick Brow Fox'


def find_lower_upper(str):
    dic = {'Upper_case':0,'Lower_case':0}

    for items in str:
        if items.isupper():
            dic["Upper_case"] += 1
        elif items.islower():
            dic["Lower_case"] += 1
    print("UPPER CASES: ", dic['Upper_case'])
    print("LOWER CASES: ", dic['Lower_case'])


find_lower_upper(str)






