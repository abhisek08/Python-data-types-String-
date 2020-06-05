'''
Write a Python program to remove existing indentation from all of the lines in a given text.
'''
import textwrap
text_='''
hello everyone this is
awesome. very awesome.let the light guid you'''
text_1=textwrap.dedent(text_)
print(text_1)