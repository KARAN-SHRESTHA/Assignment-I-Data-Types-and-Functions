""" 21. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples."""

print("Question 21")

my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def second_value(i):
    """
        the key from sorted function calls this function passing my_list -> tuple as parameter
    :param i: tuple (a,b)
    :return: last or second value of tuple
    """
    #print(i) / return i[-1], meaning last value
    return i[1]

#based on the returned last or second value of tuple it sorts out the list
print(sorted(my_list, key=second_value))
