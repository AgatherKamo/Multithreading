# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 01:40:27 2025

@author: canka
"""


import threading
#function to allow code to run concurrently
import time
#arrays
prime=[1,3,5,7,9] 
even=[2,4,6,8,10]

#function for even array
def first(arr):
    #loop to let the array iterate
    for even in arr:
        #display the numbers each after 1 second
        print(f" {even}")
        time.sleep(1)
        
  #function for even array      
def second(arr): 
    #loop to let the array iterate
    for prime in arr:
        #display the numbers each after 1 second
        print(f" {prime}")
        time.sleep(1)
        
#Thread and assign to t1, this line  lets function second run with prime as the argument
   
t1=threading.Thread(target=second, args=(prime,))

#Thread and assign to t2, this line  lets function first run with even as the argument
t2=threading.Thread(target=first, args=(even,))

#start the threads
t1.start()
t2.start()
 
   
t1.join()
t2.join()
# f=first()
#s=second()

