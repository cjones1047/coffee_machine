
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


def run_machine():

    def run_report():
        for resource in resources:
            if resource == "money":
                print(f'{resource}: ${resources[resource]}')
            else:
                print(f'{resource}: {resources[resource]}mL')

    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”. Prompt should show again after
    #  customer drink is dispensed

    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # TODO 3. Print report by user entering 'report' which shows the resources left in the coffee machine

    if user_choice == "off":
        return
    elif user_choice == "report":
        run_report()

    # TODO 4. Check if resources are sufficient to make the drink the user requests. If resources are insufficient,
    #  should print to user which resources are insufficient

    # TODO 5. If resources are sufficient, prompt user to insert coins totalling cost of drink. Calculate the total
    #  value of all coins user inserts

    # TODO 6. Check is transaction is successful by making sure that total is equal to at least as much as the cost of
    #  the drink. If what the user inserted is insufficient, then tell them it was so and refund money. If user
    #  inserted money WAS sufficient and too much, print the change being returned and add remainder to money property
    #  in resources. If user inserted money was perfect amount print nothing, just add user's charge to 'money'
    #  property.
#
    # TODO 7. Make coffee and adjust resources accordingly if the transaction was successful. After resources are
    #  deducted, print 'Here is your {user_choice}. Enjoy.' and return to asking the user what they would like.

run_machine()
