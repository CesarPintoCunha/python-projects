import secrets

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = secrets.choice(word_list)
finish_game = False
lives = 6

print(f'Pssst, the solution is {chosen_word}.')
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
      ''')


display = []
for letter in chosen_word:
    display.append("_")

while not finish_game:
    guess = input("Guess a letter: ").lower()
    
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You Lost!")
            finish_game = True        
    
    print(" ".join(display))
    

    if "_" not in display:
        finish_game = True
        print("You Won!!")

    print(stages[lives])

