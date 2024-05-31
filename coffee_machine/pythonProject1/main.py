MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 100,
}

def process_choice(customer_choice):
    if customer_choice == "off":
        print("Shutting down")
    elif customer_choice == "report":
        for item in resources:
            print(item, ":", resources[item])
    elif customer_choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            return print("Sorry there is not enough water.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            return print("Sorry there is not enough coffee")
    elif customer_choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            return print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            return print("Sorry there is not enough milk")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            return print("Sorry there is not enough coffee")
    elif customer_choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            return print("Sorry there is not enough water.")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            return print("Sorry there is not enough milk")
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            return print("Sorry there is not enough coffee")

def charge(customer_choice):
    print("Please insert coins.")
    euro_1 = int(input("how many 1 euro coins?"))
    euro50 = int(input("how many 0.50 cents coins?"))
    euro20 = int(input("how many .20 cents coins?"))
    euro10 = int(input("how many .10 cents coins?"))
    total_client = euro_1 + (0.5 * euro50) + (0.2 * euro20) + (0.10 * euro10)
    if total_client < MENU[customer_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")



machine_on = True

while machine_on:
    customer_choice = input("What would you like? (espresso/latte/cappuccino):")
    process_choice(customer_choice)
    if customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        charge(customer_choice)
    if customer_choice == "off":
        machine_on = False





