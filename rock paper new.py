import random

options = ("rock", "paper", "scissor")
play = True
while play:
    user = None
    computer = random.choice(options)
    while user not in options:
        user = input("Enter your option from - rock/paper/scissor : ")
    print(f"You choose = {user}")
    print(f"computer = {computer}")
    if user == computer:
        print("Its a tie!!")
    elif user == "scissor" and computer == "paper":
            print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win!")
    elif user == "rock" and computer == "scissor":
        print("You win!")
    else:
        print("You loose!")
    play = input("Want to play again? n to quit: ").lower()
    if play == "y":
        play = False
    else:
        play = True
print("Thanks for playing!!")