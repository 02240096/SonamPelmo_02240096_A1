
def game_menu():
    print(" Welcome the battle begins now")
    print(" Two Games")
    print(" 1. Guess the Number")
    print(" 2. Rock Paper Scissors")
    print(" 3. Exit the game")
    choice = int(input("Enter your choice: "))
    return choice 

choice = game_menu()                   #runs the menu and saves the user's choice

"""guess the number game."""
def Guess_Number_Game():
    import random                        #import random allows you to use random number functions.
    number = random.randint(1, 100)       #select a number randomly from 1 to 100
    max_attempts = 3
    attempts = 0                                    
    while attempts < max_attempts:
        try: 
            guess = int(input("Guess a number between 1 to 100:"))
            attempts += 1                                    #attempts += 1 adds 1 to the current value of attempts
            if guess < number:
               print("A bit too low! Try once more.", max_attempts - attempts, "attempts left.")
            elif guess > number:
               print("A bit too high! Try once more.", max_attempts - attempts, "attempts left.")
            else:
               print("Congratulations! You got it right in {attempts} attempts.")
               break 
        except ValueError: 
            print("Invalid input! Please enter a valid number.")

    if attempts == max_attempts and guess != number:                        # !=  Checks if two values are not equal
        print(f"Sorry! The number was, {number}. End of the game.")         #f lets you insert variables or expressions into a string.

def Rock_Paper_Scissors():
    """ Simple Rock Paper Scissors game. """
    import random 
    choices = ["rock", "paper", "scissors"]
    your_choice = input("Enter your choice: rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    print(f"Computer choice: {computer_choice}")

    if your_choice == computer_choice:
      print("It's a tie!")
    elif(your_choice == "rock" and computer_choice == "scissors") or \
        (your_choice == "paper" and computer_choice == "rock") or \
        (your_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You Lose!")
    
def Exit_program():
    print("Hope you had fun! Thanks for playing! ")
    return 

while True:
    if choice == 1:
        Guess_Number_Game()
    elif choice == 2:
        Rock_Paper_Scissors()
    elif choice == 3:
        print("Hope you had fun! Thanks for playing!")
        break 
    else:
        print("Invalid choice! Please enter a valid choice.")

    x = input("Do you wish to continue? (y/n): ")
    if x.lower() == "y":
        choice = game_menu()           #runs the menu again if the user types "y"
    else:
        Exit_program()
        break 
   