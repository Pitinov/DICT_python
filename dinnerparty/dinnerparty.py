import random
yes_no = {'yes': True, 'no': False}
number = int(input("Enter the number of friends joining (including you):\n >"))
if number < 1:
    print("No one is joining for the party")
    exit()
payment = {}
print("Enter the name of every friend (including you), each on a new line:")
for _ in range(number):
    name = input(">")
    payment[name] = 0
money = int(input("Enter the total amount:\n"))
print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
lucky = yes_no[input('>').lower()]
lucky_name = ''
if lucky:
    lucky_name = random.choice(list(payment.keys()))
    print(lucky_name, "is the lucky one!")
else:
    print("No one is going to be lucky")
a = round(money/number, 2)
for name in payment:
    payment[name] = a
