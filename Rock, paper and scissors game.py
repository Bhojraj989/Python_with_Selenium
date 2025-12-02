import random

options = ("rock","paper","scissor")

playing = True

while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Select your choice. (rock, paper and scissor) : ")

    print(f"player   : {player}")
    print(f"computer : {computer}")
    if player == computer:
        print("Its a tie")
    elif player == "paper" and computer == "rock":
        print("You win!!")
    elif    player== "rock" and computer== "scissor":
        print("You win!!")
    elif player == "scissor" and computer == "paper":
        print("You win!!")
    else:
        print("You lose!!")
    if input("Play again? n to quit) : ").lower() == "n":
        playing = False
print("Thankx for playing !! ")
