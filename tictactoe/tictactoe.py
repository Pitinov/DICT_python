game = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
def print_board(board):
    print("---------")
    for row in board:
        print("| " + " ".join(row) + " |")
    print("---------")
def valid_play(cells):
    if len(cells) != 9:
        print("There must be 9 plays")
        return False
    for letter in cells:
        if letter != 'X' and letter != 'O' and letter != '':
            print("Wrong move " + str(letter))
            return False
    return True

def update_board(row, row_number):
    game[row_number] = row


def play(cells):
    update_board(list(cells[3:]), 0)
    update_board(list(cells[3:6]), 1)
    update_board(list(cells[:3]), 2)


def game_status(game):
    winner = get_winner(game)
    if winner:
        return winner + " wins"
    if "" in game[0] or "" in game[1] or "" in game[2]:
        return "Game not finished"
    else:
        return "Draw"


def valid_game(game, cells):
    diff = cells.count('X') - cells.count('O')
    if -1 <= diff <= 1:
        wins = ""
        for row in range(0, 3):
            if game[row][0] == game[row][1] == game[row][2]:
                winner = game[row][0]
                if not wins or wins == winner:
                    wins = winner
                else:
                    return False
        for column in range(0, 3):
            if game[0][column] == game[1][column] == game[2][column]:
                winner = game[0][column]
                if not wins or wins == winner:
                    wins = winner
                else:
                    return False
        return True
    return False


def get_winner(game):
    for row in range(0, 3):
        if game[row][0] == game[row][1] == game[row][2] != '':
            return game[row][0]
    for column in range(0, 3):
        if game[0][column] == game[1][column] == game[2][column] != '':
            return game[0][column]

    if game[0][0] == game[1][1] == game[2][2] != '':
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] != '':
        return game[0][2]


def valid_coord(game, inp):
    try:
        c_x, c_y = get_coords(inp)
    except Exception:
        print("You should enter numbers!")
        return False

    if not (1 <= c_x <= 3 and 1 <= c_y <= 3):
        print("Coordinates should be from 1 to 3!")
        return False

    row, col = coords_to_row_col(c_x, c_y)
    if game[row][col] != '':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def coords_to_row_col(x, y):
    col = int(x) - 1
    row = int(y) - 1
    return row, col


def get_coords(inp):
    x, y = inp.strip().split(" ")
    return int(x), int(y)


def make_move(game, x, y, symb):
    row, col = coords_to_row_col(x, y)
    game[row][col] = symb


status = "playing"
play_round = 0
symbols = ["0", "X"]
final_status = ["Draw", "X wins", "O wins"]
print_board(game)

while status not in final_status:
    play_round = play_round + 1
    symbol = symbols[play_round % 2]
    inp = input("Enter the coordinates:")

    while not valid_coord(game, inp):
        inp = input("Enter the coordinates:")

    coord_x, coord_y = get_coords(inp)
    make_move(game, coord_x, coord_y, symbol)

    print_board(game)
    status = game_status(game)

print(status)