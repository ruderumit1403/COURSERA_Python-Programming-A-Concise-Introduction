"""
Problem 2_1:
Write a function 'problem2_1()' that sets a variable lis = list(range(20,30)) and
does all of the following, each on a separate line: 
(a) print the element of lis with the index 3
(b) print lis itself
(c) write a 'for' loop that prints out every element of lis. Recall that 
    len() will give you the length of such a data collection if you need that.
    Use end=" " to put one space between the elements of the list lis.
"""  
#%%      
def problem2_1():
    lis = list(range(20,30))
    print(lis[3])
    print(lis)
    
    for i in lis:
        print(i, end = " ")






#%%
"""
Test run:

problem2_1()
23
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
20 21 22 23 24 25 26 27 28 29 

"""