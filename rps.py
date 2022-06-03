# import random module
import random


print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

options = ['r', 'p', 's']

while True:
    print("Enter choice \n r for Rock, \n p for paper, and \n s for scissors \n")

    choice = input("User's turn: ")

    while choice not in options:
        choice = input("Please enter valid input: ")

    comp_choice = random.choice(options)

    while comp_choice == choice:
        if choice == 'r':
            choice_name = 'rock'
        elif choice == 'p':
            choice_name = 'paper'
        else:
            choice_name = 'scissors'


        print("User's choice is: " + choice_name)
        print("\nNow its computer turn.......")

        if comp_choice == 'r':
            comp_choice_name = 'rock'
        elif comp_choice == 'p':
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissors'

        print("Computer's choice is: " + comp_choice_name)

        print(f'Player ({choice_name}) : CPU ({comp_choice_name})')
        print('Match drawn, restarting game...')

        choice = input("User's turn: ")
        comp_choice = random.choice(options)

    if choice == 'r':
        choice_name = 'rock'
    elif choice == 'p':
        choice_name = 'paper'
    else:
        choice_name = 'scissors'

    print("User's choice is: " + choice_name)
    print("\nNow its the computer's turn.......")

    if comp_choice == 'r':
        comp_choice_name = 'rock'
    elif comp_choice == 'p':
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'

    print("Computer choice is: " + comp_choice_name)

    print(f'Player ({choice_name}) : CPU ({comp_choice_name})')

    if ((choice == 'r' and comp_choice == 'p') or
            (choice == 'p' and comp_choice == 'r')):
        print("paper wins => ", end="")
        result = "paper"

    elif ((choice == 'r' and comp_choice == 's') or
          (choice == 's' and comp_choice == 'r')):
        print("Rock wins =>", end="")
        result = "rock"
    else:
        print("scissor wins =>", end="")
        result = "scissors"

    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Would you like to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break


print("\nBye and thanks for playing!")
