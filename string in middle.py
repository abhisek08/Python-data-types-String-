'''
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''
def insert_string_middle(a,b):
    print(a[:2]+b+a[2:])
insert_string_middle('[[]]', 'Python')