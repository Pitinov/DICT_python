water = 400
milk = 540
cups = 9
coffe_beans = 120
money = 550
print("The coffee machine has: ")
print(water, "ml of water")
print(milk, "ml of milk")
print(coffe_beans, "g of coffee beans")
print(cups, "disposable cups")
print(money, "$ of money")
action = input("Write action (buy, fill, take):\n>")
if action == "buy":
    type_of_coffee = int(input("What do you want to buy? 1-espresso, 2-latte, 3-cappuccino:\n>"))
    if type_of_coffee == 1:
        if water >= 250 and coffe_beans >= 16 and cups >= 1:
            water -= 250
            coffe_beans -= 16
            cups -= 1
            money += 4
        elif type_of_coffee ==  2:
            if water >= 350 and milk >= 75 and cups >= 1 and coffe_beans >= 20 :
                water -= 350
                milk -= 75
                coffe_beans -= 20
                cups -= 1
                money += 7
        elif type_of_coffee == 3:
            if water >= 200 and milk >= 100 and coffe_beans >= 12 and cups >= 1:
                water -= 200
                milk -= 100
                cups -= 1
                money += 6
elif action == "fill":
    water += int(input("Write how many ml of water you want to add:\n>"))
    milk += int(input("Write how many ml of milk you want to add:\n>"))
    coffe_beans += int(input("Write how many grams of coffee beans you want to add:\n>"))
    cups += int(input("Write how many disposable coffee cups you want to add:\n>"))
elif action == "take":
    print(f"I gave you {money} ")
    money = 0
print("The coffee machine has: ")
print(water, "ml of water")
print(milk, "ml of milk")
print(coffe_beans, "g of coffee beans")
print(cups, "disposable cups")
print(money, "$ of money")