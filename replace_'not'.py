'''
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
 if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
 Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''
def replace1(str1):
    a=str1.find('not')
    b=str1.find('poor')
    if b>a and a>0 and b>0:
        str1=str1.replace(str1[a:b+4],'good')
        print(str1)
    else:
        print(str1)
replace1('The lyrics is poor!')