""" 14. Write a Python program to sort a list of dictionaries using Lambda."""

print("Question 14")

dic = {'Name':'Karan', 'Address':'Balaju', 'Age': 23}

lam = lambda x : sorted(x)

print(lam(dic))