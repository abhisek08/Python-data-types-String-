'''
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
'''
string='thequickbrownfoxjumpsoverthelazydog'
for i in string:
    a=string.count(i)
    if a>1:
        print(i,a)
