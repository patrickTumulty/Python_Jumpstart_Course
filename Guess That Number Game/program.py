import random

def Print_Header():
    print("-------------------------------")
    print("     Guess The Number Game     ")
    print("-------------------------------\n")


def Run_Game():
    mystery_number = random.randint(0, 100)
    number_guess = None
    while number_guess != mystery_number:
        number_guess = int(input("Guess a number between 0 and 100: "))
        if number_guess < mystery_number:
            print("Sorry but {} is LOWER than the number".format(number_guess))
        elif number_guess > mystery_number:
            print("Sorry but {} is HIGHER than the number".format(number_guess))
    print("\nYes! You've got it. The number was {}\n".format(mystery_number))

def main():
    Print_Header()
    Run_Game()

if __name__ == "__main__":
    main()