'''
Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters.
'''
def if_upper(str1):
    count=0
    for a in str1[0:4]:
        if a.isupper():
            count+=1
    if count>=2:
        print(str1.upper())
if_upper('Abhisek')