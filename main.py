# Importing the random module
import random

# Generating a random number between 0 and 100
rand_number = random.randint(0, 100)

# Setting the number of trials allowed
tries = 5
correct_answer = False

# Creating a while loop until either tries reach zero or correct answer is found
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

    tries -= 1
    if tries == 0:
        print("Sorry, you have 0 trials left!")
