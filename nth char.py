'''
Write a Python program to remove the nth index character from a nonempty string.
'''
def nth(n,str1):
    print(str1[:n-1]+str1[n:])
nth(3,'abhisek')