'''
Write a Python program to reverse words in a string.
'''
string='welcome to bengaluru'
lst=[]
for a in string.split():
    lst.append(a)
lst.reverse()
for a in lst:
    print(a,end=' ')