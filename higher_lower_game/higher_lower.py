import random
from game_data import data
from art import logo, vs
import os

print(logo)

end_game = False

score = 0

def random_option():
    return random.choice(data)


random_option_a = random_option()
random_option_b = random_option()

while random_option_a == random_option_b:
    random_option_b = random_option()
    
followers_option_a = random_option_a["follower_count"]
followers_option_b = random_option_b["follower_count"]

while end_game is False:
        
    print(f"Compare A: {random_option_a['name']}, a {random_option_a['description']}, from {random_option_a['country']}.")
    print(vs)
    print(f"Against B: {random_option_b['name']}, a {random_option_b['description']}, from {random_option_b['country']}.")

    player_guess = input("Who has more followers? Type 'A' or 'B': ")

    if followers_option_a > followers_option_b:
        correct_answer = "A"
    elif followers_option_b > followers_option_a:
        correct_answer = "B"
    if player_guess != correct_answer:    
        print(f"That's wrong. Final score: {score}.")
        end_game = True
    elif player_guess == correct_answer:
        score += 1 
        os.system("clear")
        print(logo)
        print(f"You're right! Current score : {score}.")
        random_option_a = random_option_b
        random_option_b = random.choice(data)
        while random_option_a == random_option_b:
            random_option_b = random_option()
        followers_option_a = random_option_a["follower_count"]
        followers_option_b = random_option_b["follower_count"]

        


  





