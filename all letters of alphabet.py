'''
 Write a Python program to check if a string contains all letters of the alphabet
'''
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string='skdfsndjgfjlgvldfjrogvnf'
for a in lst:
    if a not in string:
        print('False')
        break
    else:
        print('True')