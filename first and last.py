'''
 Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
'''
def string(str1):
    print(str1[-1]+str1[1:-1]+str1[0])
string('xaaay')