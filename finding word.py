'''
Write a Python program to count the occurrences of each word in a given sentence.
'''
def string(str1):
    lst=[]
    for a in str1.split():
        count=0
        for b in str1.split():
            if b==a:
                count+=1
        lst.append(a+':'+str(count))
    print(set(lst))
string('I am am going')