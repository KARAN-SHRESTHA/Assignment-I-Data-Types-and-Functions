""" 14. Write a Python function to create the HTML string with tags around the
word(s)."""

print("Question 14")


def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"


print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

