from art import logo
import os

print(logo)

final_dictionary = {}
highest_bid = 0
winner = ""

while True:
    
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    if bid > highest_bid:
        highest_bid = bid
        winner = name
    
    final_dictionary[name] = bid

    answer = input("Any more bidders? Type 'yes' or 'no'\n")
    if answer.lower() == "yes":
        os.system("clear")
        continue
    else:
        break


print(f"The winner is {winner} with a bid of {highest_bid}")







    