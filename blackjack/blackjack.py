import random
import os
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

def random_card():
    return random.choice(cards)

def player_move():
    if sum(player_cards) == 21:
        return dealer_move() 
    player_choice = input("Type 'y' to hit, type 'n' to stand: ")
    if player_choice == "y":
        player_cards.append(random_card())
        
        if sum(player_cards) > 21:
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
            else:
                return print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\n Your cards are over 21! You Lost!")
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Dealer first card: {dealer_cards}")    

        player_move()

def dealer_move():
    dealer_cards.append(random_card())
    print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_cards)}")
    while sum(dealer_cards) < 17:
        dealer_cards.append(random_card())
        print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_cards)}")
    if sum(dealer_cards) > 21:
        if 11 in dealer_cards:
            dealer_cards.remove(11)
            dealer_cards.append(1)
        else:
            return print("Dealer cards over 21! You Win!")
        dealer_move()

def final_result():    
    if sum(player_cards) <= 21 and sum(dealer_cards) <= 21:
        print("\nFinal Result") 
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_cards)}")
        if sum(player_cards) > sum(dealer_cards):
            return print("You Win!")
        elif sum(player_cards) < sum(dealer_cards):
            return print("You Lose!")
        else:
            return print("It's a Draw")    

def play_game():   
    
                        
    player_cards.append(random_card())
    player_cards.append(random_card())
    if sum(player_cards) > 21:
        player_cards[0] -= 10

    dealer_cards.append(random_card())
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Dealer first card: {dealer_cards}")
    player_move()
    if sum(player_cards) < 21:
        dealer_move()
    final_result()

while input("Do you Want to play Blackjack? Type 'y' or 'n': ") == "y":
    player_cards = []
    dealer_cards = []
    os.system("clear")
    play_game()
   


