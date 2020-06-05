'''
Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer. Go to the editor
Sample Output:
Input an integer: 25
Decimal Octal Hexadecimal (capitalized), Binary
25 31 19 11001
'''
n=50
print(int(50),oct(50),hex(50),bin(50))
print(int(50),oct(50)[2:],hex(50)[2:],bin(50)[2:])