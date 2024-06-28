# My messy code 😂
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


def order():
    prompt = input("What would you line? (espresso/latte/cappuccino)? ")
    return prompt.lower()

def printResources():
    global money
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffe: {resources['coffee']}")
    print(f"Money: ${money:.2f}")

def checkRequirement(chosen):
    for k, v in MENU[chosen]['ingredients'].items():
        if resources[k] < v:
            print(f"Sorry there is not enough {k}")
            return False
    return True

def processCoins():
    quarters = int(input("Insert Quarters: ")) * 0.25
    dimes = int(input("Insert Dimes: ")) * 0.1
    nickel = int(input("Insert Nickel: ")) * 0.05
    pennies = int(input("Insert Pennies: ")) * 0.01
    return quarters + dimes + nickel + pennies

def checkMoney(coins, chosen):
    return coins > MENU[chosen]['cost']

def processCoffe(coins, chosen):
    global money
    cost = MENU[chosen]['cost']
    if chosen != "espresso":
        resources['milk'] -= MENU[chosen]['ingredients']['milk']
    resources['coffee'] -= MENU[chosen]['ingredients']['coffee']
    resources['water'] -= MENU[chosen]['ingredients']['water']
    money += cost
    change = coins - cost
    print(f"Here's ${change:.2f} in change")
    print(f"Here's your {chosen} 🫕")

def processOrder(order):
    if checkRequirement(order):
        coins = processCoins()
        if checkMoney(coins, order):
            processCoffe(coins, order)
        else:
            print("Sorry that's not enough money")
    else:
        return 0

on = True
money = 0
while on:
    ask = order()
    match ask:
        case 'off':
            on = False
            print("Machine Turned Off")
            break
        case "report":
            printResources()
        case "espresso":
            processOrder(ask)
        case "latte":
            processOrder(ask)
        case "cappuccino":
            processOrder(ask)
    



