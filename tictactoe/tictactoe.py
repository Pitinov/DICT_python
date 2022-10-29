info = input('Enter cells: ')
list_of_inputs = []

for signs in info:
    list_of_inputs.append(signs)

nine_line = []
for nine_lines in range(0, 9):
    nine_line.append('-')
print("".join(nine_line[:9]))

start_index = 0
end_index = 3
for signs_inside in range(0, 3):
    print('|', ' '.join(list_of_inputs[start_index:end_index]), '|')
    start_index += 3
    end_index += 3
print("".join(nine_line[:9]))


while True:
    try:
        coordinates = list(map(int, input('Enter the coordinates: ').split()))
        actual_index = 0

        if (1 <= coordinates[0] <= 3) and 1 <= coordinates[1] <= 3:
            if coordinates == [1, 1]:
                actual_index = 0
            elif coordinates == [1, 2]:
                actual_index = 1
            elif coordinates == [1, 3]:
                actual_index = 2
            elif coordinates == [2, 1]:
                actual_index = 3
            elif coordinates == [2, 2]:
                actual_index = 4
            elif coordinates == [2, 3]:
                actual_index = 5
            elif coordinates == [3, 1]:
                actual_index = 6
            elif coordinates == [3, 2]:
                actual_index = 7
            elif coordinates == [3, 3]:
                actual_index = 8
            if list_of_inputs[actual_index] == '_':

                print("".join(nine_line[:9]))
                start_index = 0
                end_index = 3
                list_of_inputs.pop(actual_index)
                list_of_inputs.insert(actual_index, 'X')
                for signs_inside in range(0, 3):
                    print('|', ' '.join(list_of_inputs[start_index:end_index]), '|')
                    start_index += 3
                    end_index += 3
                print("".join(nine_line[:9]))

                start_index = 0
                end_index = 3
                x_count = list_of_inputs.count('X')
                o_count = list_of_inputs.count('O')

                x_winnings = 0
                o_winnings = 0
                while end_index < 9:
                    if list_of_inputs[start_index:end_index].count('X') == 3:
                        x_winnings += 1
                    elif list_of_inputs[start_index:end_index].count('O') == 3:
                        o_winnings += 1
                    start_index += 3
                    end_index += 3
                if 'X' in list_of_inputs[0] and 'X' in list_of_inputs[3] and 'X' in list_of_inputs[6]:
                    x_winnings += 1
                if 'X' in list_of_inputs[1] and 'X' in list_of_inputs[4] and 'X' in list_of_inputs[7]:
                    x_winnings += 1
                if 'X' in list_of_inputs[2] and 'X' in list_of_inputs[5] and 'X' in list_of_inputs[8]:
                    x_winnings += 1
                if 'O' in list_of_inputs[0] and 'O' in list_of_inputs[3] and 'O' in list_of_inputs[6]:
                    o_winnings += 1
                if 'O' in list_of_inputs[1] and 'O' in list_of_inputs[4] and 'O' in list_of_inputs[7]:
                    o_winnings += 1
                if 'O' in list_of_inputs[2] and 'O' in list_of_inputs[5] and 'O' in list_of_inputs[8]:
                    o_winnings += 1
                if 'X' in list_of_inputs[0] and 'X' in list_of_inputs[4] and 'X' in list_of_inputs[8]:
                    x_winnings += 1
                if 'X' in list_of_inputs[2] and 'X' in list_of_inputs[4] and 'X' in list_of_inputs[6]:
                    x_winnings += 1
                if 'O' in list_of_inputs[0] and 'O' in list_of_inputs[4] and 'O' in list_of_inputs[8]:
                    o_winnings += 1
                if 'O' in list_of_inputs[2] and 'O' in list_of_inputs[4] and 'O' in list_of_inputs[6]:
                    o_winnings += 1
                if x_count > o_count:
                    if x_count - o_count >= 2 or x_winnings + o_winnings > 1:
                        exit()
                if o_count > x_count:
                    if o_count - x_count >= 2 or x_winnings + o_winnings > 1:
                        exit()
                if x_winnings + o_winnings == 0 and list_of_inputs.count('_') > 0:
                    exit()
                if x_winnings + o_winnings == 0 and list_of_inputs.count('_') == 0:
                    exit()
                if x_winnings == 1:
                    exit()
                if o_winnings == 1:
                    exit()
            elif list_of_inputs[actual_index] != '_':
                    print('This cell is occupied! Choose another one!')
        elif (coordinates[0] < 1 or coordinates[0] > 3) or (coordinates[1] < 1 or coordinates[1] > 3):
                    print('Coordinates should be from 1 to 3!')
    except ValueError:
        print('You should enter numbers!')