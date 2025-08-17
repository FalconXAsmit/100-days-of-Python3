import random

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
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissor]
computer_choice = random.randint(0,2)
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:-\n\t"))
if human_choice >=3 or human_choice <0:
    print("Invalid input!")

print("Computer choice is:-\n" + choices[computer_choice])
print("-----------------------------------------------------------------------------------------------")
print("Human choice is:-\n" + choices[human_choice])

if human_choice == computer_choice:
    print("It's a draw")
elif human_choice == 0 and computer_choice == 2:
    print("You win!")
elif human_choice == 1 and computer_choice == 0:
    print("You won!")
elif human_choice == 2 and computer_choice == 1:
    print("You won!")
else:
    print("You lose!")