pitty = int(input("Please input your pitty"))
pulls = int(input("Please input the number of pulls you wish to do"))
if pulls >= 10: 
    print("test_1")
elif pulls < 10:
    print("test_2")
else: #will print the number of 5 stars obtained and what pulls they will get them at
    print("Your pulls are over you got")

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
