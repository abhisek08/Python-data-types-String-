'''
Write a Python program to add a prefix text to all of the lines in a string
'''
import textwrap
text_='''My name is abhisek Bhunia.
i am 28 years old.
this is awesome.
i am very good.
fine thank you'''
a='<this>'
tex_1=textwrap.indent(text_,a)
print(tex_1)