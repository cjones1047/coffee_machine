
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
    "money": 0,
}

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()


# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3. Print report
# TODO 4. Check if resources are sufficient
# TODO 5. Process coins
# TODO 6. Check is transaction is successful
# TODO 7. Make coffee and adjust resources accordingly
