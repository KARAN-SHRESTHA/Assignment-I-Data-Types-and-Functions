""" 26. Write a Python program to insert a given string at the beginning of all items in
a list."""

print("Question 26")

l = [1,2,3,4]
i = 0

for items in l:
    l[i] = 'emp' + str(items)
    i+=1
print(l)
