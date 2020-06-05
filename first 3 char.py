'''
 Write a Python function to get a string made of its first three characters of a specified string.
 If the length of the string is less than 3 then return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
'''
def first_three(str1):
    if len(str1)>=3:
        print(str1[:3])
    else:
        print(str1)
first_three('ipyd')