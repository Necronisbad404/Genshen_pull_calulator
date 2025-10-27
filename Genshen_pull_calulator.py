pitty = int(input("Please input your pitty"))
pulls = int(input("Please input the number of pulls you wish to do"))
#TO DO LIST:
    #1. Make a calculation for 10 pulls
    #2. Make a calculation for 1 pulls 
    #3. calculate the amount of 10 pulls and 1 pulls done 
    #4. 

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

def pull_10(c):
    #'c' will be the amount of 10 pulls to be done
    rand.randint(3,500)
