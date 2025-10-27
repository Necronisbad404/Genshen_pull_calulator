pitty = int(input("Please input your pitty"))
pulls = int(input("Please input the number of pulls you wish to do"))
#TO DO LIST:
    #1. Make a calculation for 10 pulls
    #2. Make a calculation for 1 pulls 
    #3. calculate the amount of 10 pulls and 1 pulls (done, needs testing)
    #4. .6% rand int generator or 3/500
    #5.

import math as mt
import random as rand
#below is a function to simulate pulls
def pull(x,z):
    # x will be pitty 
    # z will be pulls to do 
    if x >= 70: 
        #this will be the function for soft pitty 
    elif x <= 70: 
        #this will be the function for non soft pitty 
    elif x == 90: 
        #this will be hard pitty 
    else :
        print("")  

#calculates the number of single pulls and 10 pulls to do 
def pull_10_1(v): 
    #'v' will be the number of pulls 
    v = pulls
    global pulls_10 
    pulls_10 = int(v/10) #gives the number of 10 pulls to do 
    global pulls_1 
    pulls_1 = int(v%10) #gives the number of single pulls to do 

def pull_10(c):
    #'c' will be the amount of 10 pulls to be done
    rand.randint(3,500) #will not work as intended, will fix 

