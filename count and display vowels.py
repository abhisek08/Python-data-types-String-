'''
 Write a Python program to count and display the vowels of a given text.
'''
lst=['a','e','i','o','u']
c=0
text='abhisek'
for a in text:
    if a in lst:
        c+=1
        print(a)
print(c)