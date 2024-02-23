import random
rock = "Raki"
paper = "Prasad"
scissors = "Soft"
game_words = [rock, paper, scissors]

user_choice = int(input("Please choose 0:Rock, 1:Paper or 2:Scissor? (Rock/Paper/Scssors): \n"))
if user_choice >=3 or user_choice < 0:
    print("invalid number, You lose!")
else:
    print(f"Your choice is: ", game_words[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer choice is: ", game_words[computer_choice])


    if user_choice == 0 and computer_choice ==2:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice == computer_choice:
        print("Draw")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You won")
    else:
        print("You typed an invalid number")






