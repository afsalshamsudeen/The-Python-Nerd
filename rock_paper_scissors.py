#the world's finest Rock, Paper, Scissors game ever

import random

print("Welcome to the worlds finest Rock, Paper, Scissors game!")

computer_score =0
player_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice =input("Pick an option Rock/Paper/Scissors or q for quite:").lower()
    if user_choice == "q" :
        break
    if user_choice not in choices:
        print("Type something valid next time")
        continue


    random_number = random.randint(0, 2)
    computer_choice = choices[random_number]
    print("The Computer Picked", computer_choice +".")

    if user_choice == "paper" and computer_choice == "rock":
        print("You Won!")
        player_score += 1
    elif user_choice == "scissors" and computer_score == "paper":
        print("You Won!")
        player_score += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Won!")
        player_score += 1
    elif user_choice == computer_choice:
        print("Its a tie")
    else:
        print("The Computer Won!")
        computer_score +=1


print("Your Score = ",player_score)
print("The Computer's Score =",computer_score)
if computer_score > player_score:
    print("ha ha ha, human go back to worrying about your future arc!")
else:
    print("You got LUCKY!")
print("The End!")