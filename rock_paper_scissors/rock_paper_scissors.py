import random

# список опцій гри
options = ['rock', 'paper', 'scissors']

# зчитати ввід користувача
user_choice = input()

# знайти опцію, яка перемагає опцію користувача
if user_choice == 'rock':
    computer_choice = 'paper'
elif user_choice == 'paper':
    computer_choice = 'scissors'
elif user_choice == 'scissors':
    computer_choice = 'rock'
else:
    print('Invalid input. Please enter rock, paper, or scissors.')

# вивести рядок з вибором комп'ютера
print(f"Sorry, but the computer chose {computer_choice}")