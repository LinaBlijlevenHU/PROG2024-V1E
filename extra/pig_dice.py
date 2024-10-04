"""
pig_dice.py

Pig dice is a simple game where you roll 1 die until you hit 30 points total.
However, every time you hit 1, you have to restart!

Potential improvements:
- Implement a GUI for this game
- Implement some powerups: for example one to protect you from the 1 and
  another to double your next throw.
- Split up the functions better
- Add high scores that are kept in a separate file
"""
import random

# Target default is 30 points, but we could change this if we wanted to
TARGET = 30

def roll_dice():
    """ Return a random number between 1 and 6 """
    return random.randint(1, 6)

def answer_is_no(ans):
    """ Checks if the user said no """
    return ans.lower() == "n"

def play_game():
    """ Let the user roll the dice until they win! """
    points = 0
    rolls = 0

    # Let the user roll the dice until they have enough points
    while points < TARGET:
        # Wait for the user to be ready, so the game doesn't
        # automatically play by itself
        ans = input("Ready? y/n ")

        if answer_is_no(ans):
            print("Too bad, we're rolling anyway!")

        # Roll the dice and increment the counter
        res = roll_dice()
        print(f"You rolled a {res}!")
        rolls += 1

        # Is the roll 1? :(
        if res == 1:
            # Reset points
            points = 0
            print("Oh no! Your points are now reset to zero.")
        # Other rolls are added to the point total
        else:
            # Add the roll to the total
            points += res

        print(f"You have rolled {rolls} times and currently have {points}/{TARGET} points.")

    print("Wow you hit the target so lucky :D")

def main():
    # Print welcome info
    print("Welcome to pig dice! 🐷")
    print("Try to hit a score of 30 without rolling one!")

    # First time we always play of course
    play = True

    # While the user wants to play
    while play:
        # Play the game once
        play_game()

        # Ask the user to play again
        ans = input("Would you like to play again? y/n: ")

        # We only stop if the answer is a clear no
        play = not answer_is_no(ans)

""" 
We only start the program if we're using this file directly, so we can also import 
from it :)
"""
if __name__ == "__main__":
    # Hand over control to main function if we're running this file
    main()