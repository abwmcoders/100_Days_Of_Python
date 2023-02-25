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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_available(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True   

def process_coins():
     print("Please insert coins")
     total = int(input('How many quaters: ')) * 0.25
     total += int(input('How many dimes: '))* 0.1
     total += int(input('How many nickles: ')) * 0.05
     total += int(input('How many pennies: ')) * 0.01
     return total


def is_trans_succesful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change  = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost

        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")    


is_not_off = True
while is_not_off:
    choice = input('Prompt user by asking “What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'off':
        is_not_off = False
    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_available(drink['ingredients']):
            payment = process_coins()
            if is_trans_succesful(payment, drink['cost']):
                make_coffe(choice, drink['ingredients'])




