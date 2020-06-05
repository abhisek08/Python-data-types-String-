'''
Write a Python program that accepts a comma separated sequence of words as input and
prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''
def string(str1):
    lst=[]
    for a in str1.split(','):
        lst.append(a)
    sorted(lst)
    print(set(lst))
string('red, white, black, red, green, black')