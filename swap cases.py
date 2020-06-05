'''
Write a Python program to swap cases of a given string.
Sample Output:
pYTHON eXERCISES
jAVA
nUMpY
'''
str1=input('enter a string:')
b=''
for a in str1:
    if a.isupper():
        b+=a.lower()
    else:
        b+=a.upper()
print(b)