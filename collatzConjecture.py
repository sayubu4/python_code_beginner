#This program generate the collatz conjecture sequence
#The input must be greater to 2
import math
#ask the user input
n = int(input("Please enter a number "))
#create a list where to store the numbers
seq = []
#Establish the condition

for i in range(2,n):
    #if it is even
    if n % 2 == 0:
        n = int(n/2)
        #append the result
        seq.append(n)
     #if it is odd   
    else:
        n = int(3*n + 1)
        seq.append(n)

#display the results        
print(seq)

