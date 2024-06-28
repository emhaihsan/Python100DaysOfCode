from art import logo
import random
import os

def play():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {chosen_number}")

    valid = False
    while not valid:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            attempts = 10
            valid = True
        elif difficulty == "hard":
            attempts = 5
            valid = True
        else:
            print("Invalid choice, please choose between 'easy' or 'hard'")

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == chosen_number:
            print(f"You got it! The answer was {chosen_number}.")
            break
        elif guess > chosen_number:
            print("Too high.")
            attempts -= 1
        elif guess < chosen_number:
            print("Too low.")
            attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")

    restart = input("Do you want to play again? Type 'y' or 'n': ")
    if restart == "y":
        os.system('clear')
        play()
    else:
        print("Thanks for playing!")

play()