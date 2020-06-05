'''
Write a Python function to reverses a string if it's length is a multiple of 4.
'''
def rev_mul(str1):
    if len(str1)%4==0:
        print(str1[::-1])
rev_mul('abhisek')