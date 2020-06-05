'''
Write a Python program to lowercase first n characters in a string.
'''
string='ABHISEK'
n=int(input('enter number of characters to lowercase: '))
print(string[:n].lower()+string[n:])
