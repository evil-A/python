import random

x = random.randint(1, 99)
print(x)

print("This is an interactive guessing game!\n"
        "You have to enter a number between 1 and 99 to find out the secret number.\n"
        "Type 'exit' to end the game. Good luck!\n")
y = 0
z = 0

while (y != x):
    y = input("What's your guess between 1 and 99?\n")
    if (y == "exit"):
        print("Goodbye!")
        exit(0)
    try:
        z += 1
        y = int(y)
        if (y > x):
            print("too high!")
        elif (y < x):
            print("too low!")
        else:
            if (x == 42):
                print("The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulations", end="")
            if (z == 1):
                print("! You got it on your first try!")
            else:
                print(", you've got it!\nYou won in {} attemps!".format(z))
    except:
        print("That's not a number.")



