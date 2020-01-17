class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def command(self, action):
        if action == "buy":
            self.buy()

        elif action == "fill":
            self.fill()

        elif action == "take":
            self.take()

        elif action == "remaining":
            self.status()

    def espresso(self):
        if self.water < 250:
            print("Sorry, not enough water!")
        elif self.beans < 16:
            print("Sorry, not enough beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4

    def latte(self):

        if self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.beans < 20:
            print("Sorry, not enough beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7

    def cappuccino(self):

        if self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        elif self.beans < 12:
            print("Sorry, not enough beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6

    def buy(self):
        print()
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if coffee_type == '1':
            self.espresso()
        elif coffee_type == '2':
            self.latte()
        elif coffee_type == '3':
            self.cappuccino()
        else:
            self.status()

    def fill(self):
        print()
        add_water = int(input("Write how many ml of water do you want to add:"
                              ))
        add_milk = int(input("Write how many ml of milk do you want to add:"
                             ))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:"
                              ))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:"
                             ))
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.cups += add_cups

    def take(self):
        print()
        print("I gave you $" + str(self.money))
        self.money = 0

    def status(self):
        print()
        print("The coffee machine has: ")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
        print()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    action = action.lower()
    if action == "exit":
        break
    else:
        coffee_machine.command(action)
        print()
