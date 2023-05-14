#This program asks 4 questions about capital in Africa if you got one correct it is plus one otherwise it minus 1

name =input(" Welcome to capital game. What is your name? ")
print("Welcome to the capital game", name)
ques = input("Are you ready to play? (yes / no) " )
score = 0
while ques == 'yes' or ques == 'Yes':
    ques = input("1. What is the capital of Burundi ")
    if ques == "bujumbura" or ques == "Bujumbura":
        score += 1
        print("Correct")
    else:
        score -= 1
        print("Incorrect")

    ques = input("2. What is the capital of Rwanda ")
    if ques == "kigali" or ques == "Kigali":
        score += 1
        print("Good job!")
        
    else:
        score -=1
        print("Sorry! Wrong answer.")
        
    ques = input("3. What is the capital of Uganda ")
    if ques == "kampala" or ques == "Kampala":
        score += 1
        print("You were born for this game!")
        
    else:
        score -= 1
        print("Wrong answer")
        

    ques = input("4. What is the capital of Senegal ")
    if ques =="dakar" or ques == "Dakar":
        score += 1
        print("Great!")
        
    else:
        
        score -= 1
        print("nope")
    break       

print("Thank you for playing you got", score, "over 4")
