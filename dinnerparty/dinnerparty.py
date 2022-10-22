number = int(input("Enter the number of friends joining (including you):\n >" ))
if number < 1:
    print("No one is joining for the party")
    exit()
payment = {}
print("Enter the name of every friend (including you), each on a new line:")
for _ in range(number):
    name = input(">")
    payment[name] = 0
print(payment)