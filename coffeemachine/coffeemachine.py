need_water = 200
need_milk = 50
need_coffee_beans = 15
water = int(input("Write how many ml of water the coffee machine has:\n>"))
milk = int(input("Write how many ml of milk the coffee machine has:\n>"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n>"))
cups_need = int(input("Write how many cups of coffee will tou need:\n>"))
cup_coffee = min([water // need_water, milk // need_milk, coffee // need_coffee_beans])
if cup_coffee == cups_need:
    print("Yes, I can make that amount of coffee")
elif cup_coffee > cups_need:
    print("Yes, I can make that amount of coffee (and even", cup_coffee - cups_need, "morethan that)")
else:
    print("No, I can make only", cup_coffee, "cups of coffee")