'''
Write a Python function that takes a list of words and returns the length of the longest one.
'''
def longest(lst):
    b=0
    lst1=[]
    for a in lst:
        lst1.append(len(a))
    lst1.sort()
    print(lst1[-1])


lst=['aaa','aaaa','aaaaa','a']
longest(lst)