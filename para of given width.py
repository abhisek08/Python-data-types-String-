'''
Write a Python program to wrap a given string into a paragraph of given width.
Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10
Result:
The quick
brown fox.
'''
import textwrap
str1=input('Input a string: ')
w=int(input('Input the width of the paragraph: '))
print(textwrap.fill(str1,width=w))
