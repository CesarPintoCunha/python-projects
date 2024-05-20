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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_random = random.randint(0, 2)
if computer_random == 0:
    computer_choice = rock
elif computer_random == 1:
    computer_choice = paper
elif computer_random == 2:
    computer_choice = scissors

player_choice = input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if player_choice == "0":
    player_choice = rock
elif player_choice == "1":
    player_choice = paper
elif player_choice == "2":
    player_choice = scissors

print(f"You chose:\n{player_choice}")
print(f"Computer chose:\n{computer_choice}")

if player_choice == rock and computer_choice == scissors:
    print("You Win!")
elif player_choice == paper and computer_choice == rock:
    print("You Win!")
elif player_choice == scissors and computer_choice == paper:
    print("You Win!")
elif player_choice == computer_choice:
    print("It\'s a Draw!")
else:
    print("You Lose")


