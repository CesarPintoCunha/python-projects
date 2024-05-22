import secrets
import os
from art import logo, stages
from words import word_list

chosen_word = secrets.choice(word_list)
finish_game = False
lives = 6

print(logo)

#print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

while not finish_game:
    guess = input("Guess a letter: ").lower()
    os.system("clear")

    if guess in display:
            print(f"You've already guessed {guess}, chose another letter!")
    
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            print("You Lost!")
            finish_game = True        
    
    print(" ".join(display))
    

    if "_" not in display:
        finish_game = True
        print("You Won!!")

    print(stages[lives])

