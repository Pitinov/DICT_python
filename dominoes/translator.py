while True:
    language = input("Choose language (en,ua): ")
    if set(language) <= set("euua"):
        if language == "en":
            # English translations
            Hello = "Hello"
            player = "player"
            str_to_move1 = "It's your turn to make a move. Enter your command."
            str_to_move2 = "Computer is about to make a move. Press Enter to continue..."
            in_move = "Illegal move. Please try again."
            Stock_size = "Stock size"
            PC = "computer"
            us_com1 = "Invalid input.\nWrong input value range.\nPlease try again.\n> "
            us_com2 = "Invalid input.\nEnter only numbers!\nPlease try again."
            status_win = "Status: The game is over. You won!"
            status_lose = "Status: The game is over. The computer won!"
            status_draw = "Status: The game is over. It's a draw!"
            bye = "Have a nice day!"

        elif language == "ua":
            # Ukrainian translations
            Hello = "Мої вітання,козаче"
            player = "Гравець"
            str_to_move1 = "Тепер ти ходиш, обери команду"
            str_to_move2 = "Натисніть Enter, щоб комп'ютер зробив свій хід..."
            in_move = "Неможливий хід. Спробуй ще раз"
            Stock_size = "Розмір запасу"
            PC = "комп'ютер"
            us_com1 = "Недійсне введення.\nНеправильний діапазон введених значень.\nСпробуйте ще раз.\n> "
            us_com2 = "Невірне введення.\nВведіть лише цифри!\nБудь ласка, спробуйте ще раз."
            status_win = "Статус: Ти переміг, красавчик!"
            status_lose = "Статус: гра закінчена. Комп’ютер переміг!"
            status_draw = "Статус: Гра завершена. Нічия!"
            bye = "Нехай щастить"
            break
            print("Ошибка! Введите только символы eu и ua.")