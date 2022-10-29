info = input("Enter cells\n> ")

row_list = [[item for item in info[i:i + 3]] for i in range(0, 7, 3)]
col_list = [[item[i] for item in row_list] for i in range(3)]
main_diag = [[row_list[i][i] for i in range(3)]]
sec_diag = [[row_list[i][2 - i] for i in range(3)]]

game = row_list + col_list + main_diag + sec_diag
print("---------")
print("|", *row_list[0], "|")
print("|", *row_list[1], "|")
print("|", *row_list[2], "|")
print("---------")

X_NUMS = info.count("X")
O_NUMS = info.count("O")
win_x = ["X", "X", "X"]
win_o = ["O", "O", "O"]

if (win_o in game and win_x in game) or abs(X_NUMS - O_NUMS) > 1:
    print("Impossible")
elif win_o in game:
    print("O wins")
elif win_x in game:
    print("X wins")
elif "_" in info:
    print("Game not finished")
else:
    print("Draw")