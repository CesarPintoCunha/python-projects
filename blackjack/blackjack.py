import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

def random_card():
    return random.choice(cards)

player_cards.append(random_card())
player_cards.append(random_card())

dealer_cards.append(random_card())

print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
print(f"Dealer first card: {dealer_cards}")

def player_move():
    player_choice = input("Type 'y' to hit, type 'n' to stand: ")
    if player_choice == "y":
        player_cards.append(random_card())
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Dealer first card: {dealer_cards}")
        if sum(player_cards) > 21:
            return print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\n You Lost!")
        player_move()
    else:
        dealer_cards.append(random_card())
        print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_cards)}")
        while sum(dealer_cards) < 17:
            dealer_cards.append(random_card())
            print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_cards)}")
        if sum(dealer_cards) > 21:
            return print("You Win!")
    
    
    print("\nFinal Result") 
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_cards)}")
    if sum(player_cards) > sum(dealer_cards):
        return print("You Win!")
    elif sum(player_cards) < sum(dealer_cards):
        return print("You Lose!")
    else:
        return print("It's a Draw")
        
player_move()



