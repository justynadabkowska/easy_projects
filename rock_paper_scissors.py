
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
import random

computer_choice = random.randint(0, 2)

if player_choice == 0:
    print(rock)
if player_choice == 1:
    print(paper)
if player_choice == 2:
    print(scissors)

if computer_choice == 0:
    print(f"Computer chose: {rock}")
if computer_choice == 1:
    print(f"Computer chose: {paper}")
if computer_choice == 2:
    print(f"Computer chose: {scissors}")

if player_choice == 0:
    if computer_choice == 1:
        print("You lost")
    elif computer_choice == 2:
        print("You won")
    else:
        print("It's a draw")

elif player_choice == 1:
    if computer_choice == 2:
        print("You lost")
    elif computer_choice == 0:
        print("You won")
    else:
        print("It's a draw")

elif player_choice == 2:
    if computer_choice == 0:
        print("You lost")
    elif computer_choice == 1:
        print("You won")
    else:
        print("It's a draw")