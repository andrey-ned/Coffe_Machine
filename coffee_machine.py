water = 400
milk = 540
beans = 120
cups = 9
money = 550


def espresso():
    global water, beans, cups,  money
    if water < 250:
        print("Sorry, not enough water!")
    elif beans < 16:
        print("Sorry, not enough beans!")
    elif cups < 1:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water -= 250
        beans -= 16
        cups -= 1
        money += 4


def latte():
    global water, beans, cups, money, milk
    if water < 350:
        print("Sorry, not enough water!")
    elif milk < 75:
        print("Sorry, not enough milk!")
    elif beans < 20:
        print("Sorry, not enough beans!")
    elif cups < 1:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7


def cappuccino():
    global water, beans, cups, money, milk
    if water < 200:
        print("Sorry, not enough water!")
    elif milk < 100:
        print("Sorry, not enough milk!")
    elif beans < 12:
        print("Sorry, not enough beans!")
    elif cups < 1:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6


def buy():

    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if coffee_type == '1':
        espresso()
    elif coffee_type == '2':
        latte()
    elif coffee_type == '3':
        cappuccino()
    else:
        status()


def fill():
    global water, beans, cups, milk, money
    add_water = int(input("Write how many ml of water do you want to add:"
                          ))
    add_milk = int(input("Write how many ml of milk do you want to add:"
                         ))
    add_beans = int(input("Write how many grams of coffee beans do you want to add:"
                          ))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add:"
                         ))
    water += add_water
    milk += add_milk
    beans += add_beans
    cups += add_cups


def take():
    global money
    print("I gave you $" + str(money))
    money = 0


def status():
    print("The coffee machine has: ")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")
    print()


while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    action = action.lower()
    print()
    if action == "buy":
        buy()

    elif action == "fill":
        fill()

    elif action == "take":
        take()

    elif action == "remaining":
        status()
    else:
        break
