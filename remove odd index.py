'''
 Write a Python program to remove the characters which have odd index values of a given string.
'''
def string(str1):
    for i in str1:
        if str1.index(i)%2==0:
            print(i,end='')
string('abhisek')
