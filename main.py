# Importing the random module
import random


# Setting the number of trials allowed based on selected difficulty
def difficulty():
    player_choice = int(input("Choose your difficulty (Select a number)\n"
                              "1. Easy (10 tries) \n2. Medium (5 tries) \n3. Hard (3 tries)\n"))
    if player_choice == 1:
        return 10
    elif player_choice == 2:
        return 5
    elif player_choice == 3:
        return 3


def game():
    # Calling the difficulty selection at the start of the game
    tries = difficulty()

    # Generating a random number between 0 and 100
    rand_number = random.randint(0, 100)

    # Creating a while loop until either tries reach zero or correct answer is found
    correct_answer = False

    while tries > 0 and not correct_answer:
        print(f"Number of tries: {tries}")
        answer = int(input("Guess the number: "))

        if answer == rand_number:
            correct_answer = True
            print(f"Congratulations! The correct number is {rand_number}")
        elif answer > rand_number:
            print("Too High!\n")
        elif answer < rand_number:
            print("Too Low!\n")

        # Subtracting the number of trials left with each wrong answer
        tries -= 1
        if tries == 0:
            print(f"Game over, you have 0 trials left! \nThe correct number was: {rand_number}")

            # Asking the player if they want to play again otherwise game ends
            continuation = input("Would you like to play again? (y/n):").lower()
            if continuation == 'y':
                game()


game()
