import random

# список доступних варіантів гри
options = ["rock", "paper", "scissors"]

# зчитуємо введення користувача
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

# вибираємо випадковий варіант комп'ютера
computer_choice = random.choice(options)

# виводимо вибір комп'ютера
print("The computer chose:", computer_choice)

# порівнюємо варіанти користувача та комп'ютера
if user_choice == computer_choice:
    print("There is a draw ({})".format(user_choice))
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("Well done. The computer chose {} and failed".format(computer_choice))
else:
    print("Sorry, but the computer chose {}".format(computer_choice))