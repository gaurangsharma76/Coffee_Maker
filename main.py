menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


# Todo no 2: Function to check if enough ingredients are available in resources

def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item} in stock. Please contact maintenance team to refill")
            return False
        else:
            return True


# Todo no 3: Function to take money from user and check the total

def calculate_money():
    print("We only accept 10,20 50 rs denomination ")
    total_money = 0
    rs_10_note = int(input("No of Rs 10 notes"))
    rs_20_note = int(input("No of Rs 20 Notes"))
    rs_50_note = int(input("No of Rs 50 Notes"))

    total_money = rs_50_note * 50 + rs_20_note * 20 + rs_10_note * 10
    return total_money


# Todo no 4 Function to deduct the ingredient

def deduct_ingredients(req_ingredients):
    for item in req_ingredients:
        if item != "money":
            resources[item] = resources[item] - req_ingredients[item]


# TODO no 1: Print report on coffee machine resources

# Asking if customer is operating the machine or maintenance worker

user_category = input(
    "Are you customer or maintenance worker? Press 'C' for customer and 'M' for maintenance worker \n").upper()

if user_category == "M":
    switch_off = input("Type 'off' if you want to switch off machine \n")
    if switch_off == 'off':
        exit()
else:
    is_on=True
    while is_on:
        customer_input = input(
            "What would you like to have?(espresso/latte/cappuccino) or type 'report' to check available "
            "stock\n").lower()
        if customer_input == 'report':
            for i in resources:
                if i == "money":
                    print(f"{i}: Rs{resources[i]}")
                elif i == "coffee":
                    print(f"{i}: {resources[i]}gms")
                else:
                    print(f"{i}: {resources[i]}ml")
        else:

            drink = menu[customer_input]
            enough_resources = check_resources(drink['ingredients'])
            if enough_resources:
                money_paid = calculate_money()
                if money_paid < drink["cost"]:
                    print(f"The money provided was less than the cost of {customer_input}.Money refunded!!!")
                elif money_paid > drink["cost"]:
                    refund_amt = money_paid - drink["cost"]
                    print(f"Your order is being processed. Cost of drink is {drink['cost']}Here is your change of Rs{refund_amt}")
                    deduct_ingredients(drink['ingredients'])
                    print(f"Here is your {customer_input}.Enjoy!!!")
                    resources["money"]=resources["money"]+drink["cost"]
                else:
                    deduct_ingredients(drink['ingredients'])
                    print(f"Here is your {customer_input}.Enjoy!!!")
                    resources["money"] = resources["money"] + drink["cost"]
            else:
                is_on = False

