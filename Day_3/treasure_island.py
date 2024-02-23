print("Welcome to the Treasure island!")
print("Your mission is find the treasure.")

choice1 = input("You're at a cross roads, whare do you want to go? (left/right): ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake, Thare is a island in the middle of the lake and do you wanna swim or wait? (swim/wait): ").lower()
    if choice2 == "wait":
        print('Wlcome to the room')
        choice3 = input("choose the colour you want? (Yellow/Green/Red): ").lower()
        if choice3 == "yellow":
            print("treasure won")
        elif choice3 == 'red':
            print("fire")
        elif choice3 == "green":
            print("ice")
        else:
            print("You lost the game")
    else:
        print("You lost he game")
else:
    print("you are fell in to hole, Game over!")

    