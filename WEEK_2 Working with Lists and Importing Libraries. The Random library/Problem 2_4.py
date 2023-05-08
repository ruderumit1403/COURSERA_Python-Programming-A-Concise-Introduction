"""
Problem 2_4:
random.random() generates pseudo-random real numbers between 0 and 1. But what
if you needed other random reals? Write a program to use random.random() but
generate list of random reals between 30 and 35. This is a simple matter of 
multiplication and addition. Print out the list (in list form).
"""
#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    num_lis = []
    for i in range(10):
        n = (random.random() * 5 + 30)
        num_lis.append(n)
    print(num_lis)

#%%
"""
COMMENT: Note that this uses a pseudorandom number generator.  That means
that the list will be different for each person.  But all elements of the list
need to be between 30 and 35 inclusive.  How do we do that with the Coursera 
grader?
One way to handle this is to issue the command random.seed(70) inside 
problem2_4(). Then the list generated will that one given below --- always.  
You should use random.random() to generate a random number between 0 and 1 and 
then use arithmetic to convert that to a random number in the required range.

Test run:

problem2_4()
[34.54884618961936, 31.470395203793395, 32.297169396656095, 30.681793552717807,
 34.97530360173135, 30.773219981037737, 33.36969776732032, 32.990127772708405, 
 33.57311858494461, 32.052629620057274]
"""