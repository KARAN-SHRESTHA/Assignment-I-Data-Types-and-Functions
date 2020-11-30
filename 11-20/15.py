""" 15. Write a Python function to insert a string in the middle of a string.
Sample function and result :"""

print("Question 15")


def insert_string(str, word):
    return str[:2] + word + str[2:]


print(insert_string('[[]]', 'Python'))
print(insert_string('{{}}', 'PHP'))