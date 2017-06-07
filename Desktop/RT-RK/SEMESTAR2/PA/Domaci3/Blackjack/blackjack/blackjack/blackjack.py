import sys
import string
import math
import os
import struct 
import random
import numpy as np

def cmp(a, b):
    return (a > b) - (a < b) 

def BJ(i):                                                                                                                                                                                                  
    if i in BJList:                                                                                                                                                                                         
        return BJList[i]                                                                                                                                                                                    
    else:                                                                                                                                                                                                   
        options = [0]                                   # if you walk away                                                                                                                                  
        if n-i < 4:                                     # not enough cards to play                                                                                                                          
            print("NOT ENOUGH CARDS")
            return 0                                                                                                                                                                                        
        for p in range(2,(n - i)):                      # number of cards taken                                                                                                                             
            player = c[i] + c[i+2] + sum(c[i+4:i+p+2])                                                                                                                                                      
            # when p is 2         
            print("PLAYER=",player)                                                                                                                                                                          
            if player > 21:        
                print("PLAYER BUST")                                                                                                                                                                         
                options.append(-1 + BJ(i + p + 2))                                                                                                                                                          
                break                                   # breaks out of for(p)                                                                                                                              
            dealer = 0                                                                                                                                                                                      
            d1 = 0                                                                                                                                                                                          
            for d in range(2,n-i-p+1):                                                                                                                                    
                d1 = d                                                                                                                                                                                      
                dealer = c[i+1] + c[i+3] + sum(c[i+p+2:i+p+d])                                                                                                                                              
                print("DEALER=",dealer)                                                                                                                                                                               

                if dealer >= 17:                                                                                                                                                                            
                    print("DEALER STOPS DRAWING")
                    break                               # breaks out of for(d)                                                                                                                              
            if dealer < 17 and i + p + d >= n:   
                print("WHAT")                                                                                                                            
                dealer = 21                                                                                                                                          
            if dealer > 21:                      
                print("DEALER BUST")                                                                                                                                                           
                dealer = 0   
            print("DEALER=",dealer)                                                                                                                                                                               
            dealer += .5                                # dealer always wins in a tie                                                                                                                       
            options.append(cmp(player, dealer) + BJ(i + p + d1))                                                                                                                                            
        BJList[i] = (max(options))                                                                                                                                                                          
        return max(options)                                                                                                                                                                                

#c=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] 
#np.random.shuffle(c)
c=[10,7,4,2,9,6]
BJList = {}                                                                                                                                                                                                 
n = len(c)                                                                                                                                                                                                  
print ("array:" +  str(c))                                                                                                                                                                                    
print (BJ(0))  
