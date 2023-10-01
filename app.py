import random
def mann() :
    player_choice=input("enter a choice (rock,paper,scissor) : ") 
    option=["rock","paper","scissor"]
    computer_choice=random.choice(option)
    choices= {"player":player_choice, "computer": computer_choice}
    return choices

def check_win(player ,computer):
    print("you choose  " +  player  + " computer choose  " + computer )
    if player==computer:
        return "its a tie"
    elif player=="rock":
        if computer== "scissor":
            return "rock smash the scissor ! you win"
        else:
            return "paper cover rock ! you lose "
    elif player=="paper":
        if computer== "rock":
            return "paper cover rock ! you win"
        else:
            return "scissor cuts paper ! you lose "
    elif player=="scissor":
        if computer== "paper":
            return "scissor cuts paper ! you win"
        else:
            return "rock smash scissor! you lose "    
        
choices= mann()
result= check_win(choices["player"], choices["computer"])
print(result)    
    
# dict={"name":"chyy","color":choice}
# print(dict)

# abc= input("enter a number : ")
# print(abc)

# food=["egg","fish","butter"]
# dinner= random.choice(food)
# print(dinner)

# age=20
# if age>=21:
#     print("young")
# elif age>10:
#     print("teenager")
# elif age>1:
#     print("child")        
# else :
#     print("underage")    

