from random import randint

from art import logo

number = randint(1, 100)
attempts = 0
end_game = False

print(logo)
print("Welcome to the Number Guessing Game!\nGuess a number between 1 and 100.")
print(number)

def choose_difficulty():
    difficulty = input("Choose  difficulty. Type 'easy' or 'hard': ")
    if difficulty != "easy" and difficulty != "hard":
        print("Not a valid option")
        return choose_difficulty() 
    if difficulty == 'easy':
        print("You have 10 attempts remaining")
        return attempts + 10
    elif difficulty == 'hard':
        print("You have 5 attempts reamining")
        return attempts + 5
      
attempts = choose_difficulty()

while end_game is False:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You Win! The answer was {number}.")
        end_game = True
    elif guess > number:
        attempts -= 1
        if attempts == 0:
            print("Too high.\nYou've run out of guesses, you lose.")
            end_game = True
        else:
            print("Too high.\nGuess again.")
            print(f"You have {attempts} attempts remaining.")
    elif guess < number:
        attempts -= 1
        if attempts == 0:
            print("Too low.\nYou've run out of guesses, you lose.")
            end_game = True
        else:
            print("Too low.\nGuess again.")
            print(f"You have {attempts} attempts remaining.")
        
        



 

