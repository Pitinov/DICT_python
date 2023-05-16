import random

# зчитати рейтинг з файлу rating.txt
with open("rating.txt", "r") as file:
    rating = dict(line.strip().split() for line in file)

# запустити гру
name = input("Enter your name: ")
print(f"Hello, {name}")

# отримати початковий бал користувача
user_score = int(rating.get(name, 0))

while True:
    user_input = input()

    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {user_score}")
    elif user_input in ["rock", "paper", "scissors"]:
        options = ["rock", "paper", "scissors"]
        computer_option = random.choice(options)

        if user_input == computer_option:
            print(f"There is a draw ({computer_option})")
            user_score += 50
        elif (user_input == "rock" and computer_option == "scissors") or \
             (user_input == "paper" and computer_option == "rock") or \
             (user_input == "scissors" and computer_option == "paper"):
            print(f"Well done. The computer chose {computer_option} and failed")
            user_score += 100
        else:
            print(f"Sorry, but the computer chose {computer_option}")
    else:
        print("Invalid input")

# зберегти оновлений рейтинг у файл rating.txt
with open("rating.txt", "w") as file:
    for player, score in rating.items():
        if player == name:
            score = user_score
        file.write(f"{player} {score}\n")