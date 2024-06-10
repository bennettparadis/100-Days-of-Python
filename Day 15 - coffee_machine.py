RECIPES = {
    'espresso' : {
        'ingredients': { 'water': 50, 'coffee' : 18, 'milk':0},
        'cost' : 1.50
        },
    'latte' : {
        'ingredients' : {'water' : 200, 'coffee':24, 'milk':150 },
        'cost' : 2.50
        },
    'cappuccino' : {
        'ingredients' : {'water' : 250, 'coffee':24, 'milk':100 },
        'cost' : 3.00
        },
    }


def check_reserves(drink):
    for item in drink['ingredients']:
        if drink['ingredients'][item] > reserves[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True          


#print report if user types 'report'
def print_report():
    print(f"Water : {reserves['water']}ml")
    print(f"Milk : {reserves['milk']}ml")
    print(f"Coffee : {reserves['coffee']}g")
    print(f"Money : ${profit}")


profit = 0
reserves = {
    'water': 300,
    'milk' : 200,
    'coffee' : 100,
}

is_on = True

while is_on:

    #user makes choice
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice in RECIPES:

        drink_recipe = RECIPES[choice]
        drink_price = RECIPES[choice]['cost']

        if not check_reserves(drink_recipe):
            continue  # Skip the rest of the loop if there's not enough of an ingredient

        check_reserves(drink_recipe)
        print("Please insert coins.")
        Qs = int(input("How many quarters?: "))
        Ds = int(input("How many dimes?: "))
        Ns = int(input("How many nickels?: "))
        Ps = int(input("How many pennies?: "))

        #add sum
        total_paid = (0.25*Qs) + (0.1*Ds) + (0.05*Ns) + (0.01*Ps)

        #check if total_paid is enough
        if total_paid < drink_price:
            print("Sorry that's not enough money. Money refunded.")
        else:
            #if it is enough, return change if there is any
            change = "{:.2f}".format(total_paid - drink_price) #beginning part rounds and displays 2 decimal places
            profit += drink_price
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice}. Enjoy!")


        #get the ingredient dictionary for the items used in the order
        used_ingredients = drink_recipe['ingredients'] 
        #dictionary comprehension to update the quantities in the machines reserves
        reserves = {key: reserves[key] - used_ingredients.get(key,0) for key in reserves.keys()}
    
    elif choice == 'report':
        print_report()
    
    elif choice == 'off':
        is_on = False
    else:
        print("I'm sorry, I don't know what that is. You see, I only make a few coffee bevarges...")



