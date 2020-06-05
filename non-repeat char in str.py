'''
Write a Python program to find the first non-repeating character in given string.
'''
string='aabhisek'
for a in string:
    if string.count(a)==1:
        print(a)
        break