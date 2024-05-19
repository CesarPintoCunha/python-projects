print("Welcome to the tip calculator!")

total = float(input("What was the total bill?\n"))

tip = int(input("How much tip would you like to give?\n"))

people = int(input("How many people to split the bill?\n"))

final = (((tip/100) * total) + total) / people

final_round = round(final, 2)

final_round = "{:.2f}".format(final)

print(f"Each person should pay: {final_round}€")


