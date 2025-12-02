import random
import time

roll = input("Enter to roll, q to quit")

d = 0.1
while True:
    if not roll == "q":
        dice = random.randint(1, 6)
        time.sleep(d)
        print("Rolling")
        while d <= 0.5:
            print("*", end=" ")
            time.sleep(0.4)
            d += d
        print(dice)
        roll = input("Enter to roll, q to quit")
        d = 0.1
    else :
        break

