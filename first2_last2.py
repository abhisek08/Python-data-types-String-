'''
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''
def first2_last2(string):
    if len(string)<2:
        print('Empty String')
    else:
        print(string[0:2]+string[-2:])
first2_last2('w')