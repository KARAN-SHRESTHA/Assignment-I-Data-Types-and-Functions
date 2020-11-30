""" 8. Write a Python program to remove the nth index character from a nonempty
string."""

print("Question 8")

str = input("Input a string.")
num = int(input("Enter the index number which you want to remove."))

initial_char = str[:num]
final_char = str[num+1:]
char = initial_char + final_char

print(char)