#This program generates the fibonacci sequence
#ask the user input
n = int(input("Enter a number of your choice: "))
#variable assignment
i_value = 0
f_value = 1
#Establish the condition
for i in range(1,n):
    fibonnaci = i_value + f_value
    i_value = f_value
    f_value = fibonnaci
#Display the result
    print(fibonnaci)
