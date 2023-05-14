#This program generates prime factors of a given numbr
#ask the user input
n = int(input("Enter a number: "))
#divisor 
d = 2
#create a list 
seq = []
#Establish the condition
while d <= n:
    if n % d == 0:
        seq.append(d)
        #update the divisor
        n = n / d      
    else:
        d = d + 1
#display the results
print(seq)
