# Python Program for Guess the Number.
import random

def guess_the_Number():
    print(f"{"*"*10}Welcome to the Guess the Number{"*"*10}")

    number=random.randint(1,100)
    attempts=10
    while attempts>0:
        try:
            guess=int(input(f"You have {attempts} attempts left.Enter you Guess(1-100):"))
        except ValueError:
            print("Inavalid Input,Please enter an Integer.")
            continue
        if guess > number:
            print("Too High!")
        elif guess < number:
            print("Too Low!")
        else:
            print(f"Correct! You guessed the correct number: {guess}")
            break
        attempts-=1
    if attempts==0:
        print(f"Sorry, you've run out of attempts. The correct number was {number}.")
        
guess_the_Number()