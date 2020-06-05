'''
Write a Python program to remove a newline in Python.
'''
def newline(str1):
    a=str1.find('/n')
    print(str1[:a])
newline('python/n')
