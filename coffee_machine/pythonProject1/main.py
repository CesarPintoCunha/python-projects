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
}

money = 100


def process_choice(customer_choice):
    if customer_choice == "off":
        print("Shutting down")
    elif customer_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: {money}€")
    elif customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        drink = MENU[customer_choice]["ingredients"]
        for item in drink:
            if drink[item] > resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

            return True



def charge(customer_choice):
    print("Please insert coins.")
    euro_1 = int(input("how many 1 euro coins?"))
    euro50 = int(input("how many 0.50 cents coins?"))
    euro20 = int(input("how many .20 cents coins?"))
    euro10 = int(input("how many .10 cents coins?"))
    total_client = euro_1 + (0.5 * euro50) + (0.2 * euro20) + (0.10 * euro10)
    profit = MENU[customer_choice]["cost"]
    change = round(total_client - MENU[customer_choice]["cost"], 2)
    if total_client < MENU[customer_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total_client >= MENU[customer_choice]["cost"]:
        print(f"Here is {change}€ in change.")
        print(f"Here is your {customer_choice} ☕️. Enjoy!")
        global money
        money += profit


def resources_used(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]


machine_on = True

while machine_on:
    customer_choice = input("What would you like? (espresso/latte/cappuccino):")
    process_choice(customer_choice)
    if customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        if process_choice(customer_choice):
            charge(customer_choice)
            resources_used(MENU[customer_choice]["ingredients"])
    if customer_choice == "off":
        machine_on = False
 





