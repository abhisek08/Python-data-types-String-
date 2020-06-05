'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''
def swap(str1,str2):
    print(str2[0:2]+str1[2:]+' '+str1[0:2]+str2[2:])
swap('abcc','xyzz')