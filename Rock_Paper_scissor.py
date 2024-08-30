import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


print("Please enter your choice")
myChoice = int(input("for rock = 0, paper = 1, scissors= 2\n"))
if myChoice == 0:
    print("You choose rock")
    print(rock)
elif myChoice == 1:
    print("You choose paper")
    print(paper)
else:
    print("You choose scissors")
    print(scissors)

random_computer_choice = random.randint(0, 2)
if random_computer_choice == 0:
    print("Computer choose rock")
    print(rock)
elif random_computer_choice == 1:
    print("Computer choose paper")
    print(paper)
else:
    print("Computer choose scissors")
    print(scissors)

if myChoice == 0 and random_computer_choice == 0:
    print("It's a tie!")
elif myChoice == 0 and random_computer_choice == 1:
    print("Paper covers rock, computer wins!")
elif myChoice == 0 and random_computer_choice == 2:
    print("Rock smashes scissors, you win!")
elif myChoice == 1 and random_computer_choice == 0:
    print("Paper covers rock, you win!")
elif myChoice == 1 and random_computer_choice == 1:
    print("It's a tie!")
elif myChoice == 1 and random_computer_choice == 2:
    print("Scissors cuts paper, computer wins!")
elif myChoice == 2 and random_computer_choice == 0:
    print("Rock smashes scissors, computer wins!")
elif myChoice == 2 and random_computer_choice == 1:
    print("Scissors cuts paper, you win!")
elif myChoice == 2 and random_computer_choice == 2:
    print("It's a tie!")
else:
    print("Invalid input")
