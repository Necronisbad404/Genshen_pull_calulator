#all variables defined 
pitty = int(input("Please input your pitty"))
pulls = int(input("Please input the number of pulls you wish to do"))
five_stars = 0
five_stars_pitty = 0
four_stars = 0
four_stars_pitty = 0
#TO DO LIST:
    #1. Make a calculation for 10 pulls
    #2. Make a calculation for 1 pulls 
    #3. calculate the amount of 10 pulls and 1 pulls (done, needs testing)
    #4. .6% rand int generator or 3/500
    #5. add more falsafe mesure 
    #6. Make calculations for 5* curbed pulls
    #7. note what pulls got 5*'s

import math as mt
import random as rand
#below is a function to simulate pulls
def pull(x,z):
    pull_10_1(z) # will add the 2 varables for 1 and 10 pulls 
    # x will be pitty 
    # z will be pulls to do 
    if x == 90:
        print("placeholder")
        five_stars += 1
        five_stars_pitty = 0
        #this will be hard pitty 
    while x >= 70: 
        print("placeholder")
        #this will be the function for soft pitty 
    while x <= 70: 
        while pulls_10 >=0:
            pull_10(1)
            pulls_10 -= 1
            x += 10
        if pulls_10 == 0:
            while pulls_1 >= 0: 
                pull_1(1) 
                pulls_1 -= 1
                x +=1
        print("placeholder")
        #this will be the function for non soft pitty 
    
    else : # add more falisafes mesure 
        print("invalid input please try again or contact me at necronisbad404@gmail.com")
#program for 10 pulls to caculate off of 
def pull_10_program():
        v = 10
        while v > 0:
            z = rand.randint(1,167) # is very slightly off by ~.00002
            x = rand.randint(1,20)# off by about ~0.4 ## will look into making more precsies
            if z == 167:
                five_stars += 1 
                five_stars_pitty = 0
            else: 
                pass
            if x == 20:
                four_stars += 1 
                four_stars_pitty += 1
            else:
                pass 
            v -= 1
#calculates the number of single pulls and 10 pulls to do 
def pull_10_1(v): 
    #'v' will be the number of pulls 
    v = pulls
    global pulls_10 
    pulls_10 = int(v/10) #gives the number of 10 pulls to do 
    global pulls_1 
    pulls_1 = int(v%10) #gives the number of single pulls to do 

def pull_1(c):
    #'c' will be the amount of 1 pulls to be done
    # needs to be a 3/500 odds how to get 3/500 = 1/167
    c = pull_1
    while c > 0:
        z = rand.randint(1,167) # is very slightly off by ~.00002
        x = rand.randint(1,20)# off by about ~0.4 ## will look into making more precsies
        if z == 167:
            five_stars += 1 
            five_stars_pitty = 0
        else: 
            pass
        if four_stars_pitty == 0: 
            four_stars += 1
            four_stars_pitty = 0
        elif x == 20:
            four_stars += 1 
            four_stars_pitty += 1
        else:
            pass 
        c -= 1
        five_stars_pitty += 1

def pull_10(g):
    #'g' will be the number of 10 pulls to do 
    while g > 0: 
        pull_10_program()
        four_stars += 1
        four_stars_pitty = 0 
        g -= 1




