# Python program for Dice Roll
import random

def roll_dice(num_dice, num_sides):
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results

def main():
    print("\033[1;33mWelcome to the Dice Roll Simulator!\033[0m")
    
    while True:
        try:
            num_dice = int(input("\033[1mEnter the number of dice to roll: \033[0m"))
            num_sides = int(input("\033[1mEnter the number of sides per die: \033[0m"))
            if num_dice < 1 or num_sides < 2:
                print("Please enter valid numbers (at least 1 die and 2 sides per die).")
                continue
            
            results = roll_dice(num_dice, num_sides)
            print(f"\033[1;32mYou rolled: {results}\033[0m")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        again = input("\033[1;31mRoll again? (yes/no): \033[0m").strip().lower()
        if again != 'yes':
            print("\033[1;35mThanks for playing!\033[1;31m")
            break

if __name__ == "__main__":
    main()
