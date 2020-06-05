'''
 Write a Python function to get a string made of 4 copies of the last two characters of a specified string
 (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
'''
def insert_end(str1):
    if len(str1)>=2:
        print(str1[-2:]*4)
    else:
        print('invalid input')
insert_end('Py')