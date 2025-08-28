# Coffee Machine
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
    },
}
profit = 0
resources = {
    "water": 2000,
    "milk": 700,
    "coffee": 600,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    print("Please insert coin")
    total = 0
    total += int(input("Enter number of Quaters: ")) * 0.25
    total += int(input("Enter number of Dimes: ")) * 0.1
    total += int(input("Enter number of Nickels: ")) * 0.05
    total += int(input("Enter number of Pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink):
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


machine_on = True

while machine_on:
    print(f"Espresso: {MENU['espresso']['cost']}")
    print(f"Latte: {MENU['latte']['cost']}")
    print(f"Cappuccino: {MENU['cappuccino']['cost']}")

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print(f"Water left is {resources['water']}")
        print(f"Milk left is {resources['milk']}")
        print(f"Coffee left is {resources['coffee']}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
